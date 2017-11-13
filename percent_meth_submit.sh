#!/bin/bash                         

#$ -S /bin/bash                     
#$ -cwd                            
#$ -r y                            
#$ -j y                           
#$ -l mem_free=20G                 
#$ -l arch=linux-x64               
#$ -l netapp=2G,scratch=2G         
#$ -l h_rt=24:00:00   
#$ -t 1-115   




scl enable python33 'python percent_meth_2.py $SGE_TASK_ID'
