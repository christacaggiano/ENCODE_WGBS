#!/bin/bash

### Variables passed from the previous script call_trim_galore_bismark_alignment.sh retained:
INPUT_FILE_R1=$1
INPUT_FILE_R2=$2
OUTPUT_DIR=$3
CURRENT_WD=$4

source $CURRENT_WD"/qsub_submit.sh"

### Set the temporary dir:
TEMP_DIR=$5

### Run trim galore on each splitted paired-end fastqs with 18 million reads, and clip 4-bp from each end to get rid of any poor read quality bias: 
$TRIMGALORE_PATH/trim_galore -o $TEMP_DIR --dont_gzip --clip_R1 4 --clip_R2 4 --three_prime_clip_R1 4 --three_prime_clip_R2 4 --paired $INPUT_FILE_R1 $INPUT_FILE_R2

echo "Here are the trimmed files:"
ls -l $TEMP_DIR

### Set names to trimmed fastqs for read_1 and read_2:
TRIMMED_R1=$TEMP_DIR/$(basename $INPUT_FILE_R1 .fastq.gz)_val_1.fq  ### read_1
TRIMMED_R2=$TEMP_DIR/$(basename $INPUT_FILE_R2 .fastq.gz)_val_2.fq  ### read_2

### Run bismark alignment on paired-end trimmed fastqs (read_1 & read_2) using bowtie-2:
$BISMARK_PATH/bismark --bowtie2 -p 8 --bam --temp_dir $TEMP_DIR --path_to_bowtie $BOWTIE_PATH/ -o $OUTPUT_DIR $GENOME_PATH -1 $TRIMMED_R1 -2 $TRIMMED_R2
