#!/bin/sh                         
#PBS -A UQ-IMB-CNSG                                               
#PBS -l select=1:ncpus=1:mem=5gb                     
#PBS -l walltime=336:00:00
#PBS -N parallel_align

cd /30days/uqfgarto/ENCODE_WGBS

output=$1
script_dir=$2
name=$3

fastq_files=($(ls -d $name*R1*))

fq1=${fastq_files[$PBS_ARRAYID-1]}
fq2=${fq1/R1/R2}

echo $fq1

$script_dir/trim_galore_bismark_alignment.sh $fq1 $fq2 $output"/bam_files" $output"/temp_dir"

echo "finished"

