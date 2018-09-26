################ qsub parameters ###########################
#!/bin/sh                                                
#PBS -l select=1:ncpus=1:mem=1gb  # amount of memory needed
#PBS -r y                            
#PBS -j y                          
#PBS -e log_files  # where to put error messages
#PBS -o log_files  # where to put output messages
#PBS -l walltime=336:00:00  # max amount of time pipeline should run 

 
cd /30days/uqfgarto/ENCODE_WGBS/

fastq_directory=$1

conda activate py37

for fastq in $fastq_directory/*f*q*; do
    fastqc $fastq
done
