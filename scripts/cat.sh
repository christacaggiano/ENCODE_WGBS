#!/bin/sh                     
#PBS -A UQ-IMB-CNSG
#PBS -l walltime=24:00:00
#PBS -l select=1:ncpus=1:mem=5gb
#PBS -N concat 
#PBS -t 1-8

cd /30days/uqfgarto/fastqc_firstrun


cat $PBS_ARRAYID"_BC"*R1*.fastq.gz > $PBS_ARRAYID.R1.fq.gz
cat $PBS_ARRAYID"_BC"*R2*.fastq.gz > $PBS_ARRAYID.R2.fq.gz

