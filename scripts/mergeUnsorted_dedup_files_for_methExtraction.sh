#!/bin/bash
 
OUTPUT_DIR=$1
BAM_DIR=$2
LIB=$3
CURRENT_WD=$4

source $CURRENT_WD"/qsub_submit.sh"

echo "$OUTPUT_DIR"

BAM_COUNT=$( ls $BAM_DIR/*.bam | wc -l)

### Merge the unsorted bam files:
if [[ $BAM_COUNT > 1 ]]; then
            BAM_LIST=$( ls $BAM_DIR/*.bam | tr '\n' ' ' )
            $SAMTOOLS_PATH/samtools merge -nf $OUTPUT_DIR/unsortedButMerged_ForBismark_file/${LIB}_unsorted_merged.bam $BAM_LIST

    else if [[ $BAM_COUNT = 1 ]]; then
            cp $BAM_DIR/*.bam $OUTPUT_DIR/unsortedButMerged_ForBismark_file/${LIB}_unsorted_merged.bam
            
	fi      
fi     

### Run the deduplication, and remove the pcr duplicates from unsorted_bam_files (i.e the sequence aligning to the same genomic positions).
$BISMARK_PATH/deduplicate_bismark -p --bam $OUTPUT_DIR/unsortedButMerged_ForBismark_file/${LIB}_unsorted_merged.bam --output_dir $OUTPUT_DIR/unsortedButMerged_ForBismark_file

BAM_PATH=$OUTPUT_DIR/unsortedButMerged_ForBismark_file

if [[ ! -d $OUTPUT_DIR/unsortedButMerged_ForBismark_file ]]; then
	mkdir $OUTPUT_DIR/$unsortedButMerged_ForBismark_file
fi

if [[ ! -d $OUTPUT_DIR/unsortedButMerged_ForBismark_file/methylation_extraction ]]; then	
	mkdir $OUTPUT_DIR/unsortedButMerged_ForBismark_file/methylation_extraction
fi

### Set the output dir to retain all the methylation called file:
METH_OUTPUT_DIR=$OUTPUT_DIR/unsortedButMerged_ForBismark_file/methylation_extraction

### BAM files should be unsorted, and Default = CpG context only; else use --CX_context for all CpG info.
for bam_file in $(ls $BAM_PATH/*_unsorted_merged.deduplicated.bam); do
	$BISMARK_PATH/bismark_methylation_extractor -p --no_overlap -o $METH_OUTPUT_DIR --comprehensive --report --bedGraph --genome_folder $GENOME_PATH $bam_file	
	echo ""
done

