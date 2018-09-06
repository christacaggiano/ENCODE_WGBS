#!/bin/bash                         

#$ -S /bin/bash                     
#$ -cwd                            
#$ -r y                            
#$ -j y                           
#$ -l mem_free=15G                 
#$ -l arch=linux-x64               
#$ -l netapp=2G,scratch=2G         
#$ -l h_rt=336:00:00
#$ -t 9:10  

input="/ye/zaitlenlabstore/christacaggiano/cfDNA_project/second_primary_methylation_data_ALS/fastq_files/zaitlenn-"$SGE_TASK_ID"_BC"
output="/zaitlen/netapp/group/christa"
fastq_prefix=$SGE_TASK_ID
scripts="scripts"

python wgbs.py $input $output $fastq_prefix 
