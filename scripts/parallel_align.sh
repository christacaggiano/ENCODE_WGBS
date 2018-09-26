#!/bin/bash                         

#$ -S /bin/bash                     
#$ -cwd                            
#$ -r y                            
#$ -j y
#$ -l mem_free=5G                 
#$ -l arch=linux-x64               
#$ -l netapp=2G,scratch=2G         
#$ -l h_rt=336:00:00

output=$1
script_dir=$2
name=$3

fastq_files=($(ls -d $name*R1*))

fq1=${fastq_files[$SGE_TASK_ID-1]}
fq2=${fq1/R1/R2}

echo $fq1

$script_dir/trim_galore_bismark_alignment.sh $fq1 $fq2 $output"/bam_files" $output"/temp_dir"

echo "finished"

