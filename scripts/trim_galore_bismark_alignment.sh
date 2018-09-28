#!/bin/sh                                                
#PBS -A UQ-IMB-CNSG
#PBS -l select=1:ncpus=1:mem=5gb                    
#PBS -l walltime=336:00:00
#PBS -N trim_galore_bismark_alignment

cd /30days/uqfgarto/ENCODE_WGBS

### Variables passed from the previous script call_trim_galore_bismark_alignment.sh retained:
NAME=$1
OUTPUT_DIR=$2
CURRENT_WD=$3
TEMP_DIR=$4
ID=$5

source $CURRENT_WD/runWGBS

fastq_files=($(ls -d $OUTPUT_DIR/$NAME*R1*))

fq1=${fastq_files[$ID]}
fq2=${fq1/R1/R2}

$TRIMGALORE_PATH/trim_galore -o $TEMP_DIR --dont_gzip --clip_R1 4 --clip_R2 4 --three_prime_clip_R1 4 --three_prime_clip_R2 4 --paired $fq1 $fq2

### Set names to trimmed fastqs for read_1 and read_2:
TRIMMED_R1=$TEMP_DIR/$(basename $INPUT_FILE_R1 .fastq.gz)_val_1.fq 
TRIMMED_R2=$TEMP_DIR/$(basename $INPUT_FILE_R2 .fastq.gz)_val_2.fq  

### Run bismark alignment on paired-end trimmed fastqs (read_1 & read_2) using bowtie-2:
$BISMARK_PATH/bismark --bowtie2 -p 8 --bam --temp_dir $TEMP_DIR --path_to_bowtie $BOWTIE_PATH/ -o $OUTPUT_DIR $GENOME_PATH -1 $TRIMMED_R1 -2 $TRIMMED_R2

# rm $TRIMMED_R1
# rm $TRIMMED_R2 

# rm $fq1
# rm $fq2 
