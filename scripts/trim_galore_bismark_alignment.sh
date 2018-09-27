#$ -S /bin/bash                     
#$ -cwd                            
#$ -r y                            
#$ -j y
#$ -l mem_free=5G                 
#$ -l arch=linux-x64               
#$ -l netapp=2G,scratch=2G         
#$ -l h_rt=336:00:00

fq1=$1
fq2=$2
bam_dir=$3
temp_dir=$4
wd=$5

source $wd/runWGBS


# ### Run trim galore on each splitted paired-end fastqs with 18 million reads, and clip 4-bp from each end to get rid of any poor read quality bias: 
$TRIMGALORE_PATH/trim_galore -o $TEMP_DIR --dont_gzip --clip_R1 4 --clip_R2 4 --three_prime_clip_R1 4 --three_prime_clip_R2 4 --paired $fq1 $fq2

# echo "Here are the trimmed files:"
# ls -l $TEMP_DIR

# ### Set names to trimmed fastqs for read_1 and read_2:
TRIMMED_R1=$TEMP_DIR/$(basename $fq1 .fastq.gz)_val_1.fq  ### read_1
TRIMMED_R2=$TEMP_DIR/$(basename $fq2 .fastq.gz)_val_2.fq  ### read_2

echo $OUTPUT_DIR 

### Run bismark alignment on paired-end trimmed fastqs (read_1 & read_2) using bowtie-2:
$BISMARK_PATH/bismark --bowtie2 -p 12 --bam --temp_dir $TEMP_DIR --path_to_bowtie $BOWTIE_PATH/ -o $bam_dir $GENOME_PATH -1 $TRIMMED_R1 -2 $TRIMMED_R2

