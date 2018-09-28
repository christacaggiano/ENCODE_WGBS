#!/bin/sh
#PBS -A UQ-IMB-CNSG
#PBS -l walltime=336:00:00                                                
#PBS -l select=1:ncpus=1:mem=1gb                     
#PBS -e log_files  
#PBS -o log_files  
#PBS -N fastqc 

 
cd /30days/uqfgarto/ENCODE_WGBS

fastq_directory=$1

conda activate py37

for fastq in $fastq_directory/*f*q*; do
    fastqc $fastq
done
