#$ -S /bin/bash                     
#$ -cwd                            
#$ -r y                            
#$ -j y                           
#$ -l mem_free=5G                 
#$ -l arch=linux-x64               
#$ -l netapp=2G,scratch=2G         
#$ -l h_rt=24:00:00 
#$ -t 1:8   


cat $SGE_TASK_ID"_BC"*R1*.fastq.gz > $SGE_TASK_ID.R1.fq.gz
cat $SGE_TASK_ID"_BC"*R2*.fastq.gz > $SGE_TASK_ID.R2.fq.gz

