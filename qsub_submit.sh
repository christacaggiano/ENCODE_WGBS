#!/bin/bash                         

#$ -S /bin/bash                     
#$ -cwd                            
#$ -r y                            
#$ -j y                           
#$ -l mem_free=20G                 
#$ -l arch=linux-x64               
#$ -l netapp=2G,scratch=2G         
#$ -l h_rt=24:00:00      
#$ -t 1-114



python wgbs_last_step.py  /ye/zaitlenlabstore/cfDNA/fastq /ye/zaitlenlabstore/christacaggiano/dna-me-pipeline/HAIB/bismark_pipeline $SGE_TASK_ID 
