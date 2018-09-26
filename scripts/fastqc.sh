################ qsub parameters ###########################
#$ -S /bin/bash                     
#$ -cwd  # run in current directory                         
#$ -r y                            
#$ -j y                           
#$ -l mem_free=1G  # amount of memory needed                
#$ -l arch=linux-x64               
#$ -l netapp=2G,scratch=2G  
#$ -e log_files  # where to put error messages
#$ -o log_files  # where to put output messages
#$ -l h_rt=336:00:00  # max amount of time pipeline should run 

fastq_directory=$1

conda activate py37 

for fastq in $fastq_directory/*f*q*; do 
    fastqc $fastq
done


