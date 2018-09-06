#!/bin/bash                         

################ qsub parameters ###########################
#$ -S /bin/bash                     
#$ -cwd                             
#$ -r y                            
#$ -j y                           
#$ -l mem_free=15G                 
#$ -l arch=linux-x64               
#$ -l netapp=2G,scratch=2G         
#$ -l h_rt=336:00:00
#$ -t 9:10  

################## environment ###############################
GENOME_PATH="/ye/zaitlenlabstore/christacaggiano/hg38/"
BISMARK_PATH="/ye/zaitlenlabstore/christacaggiano/Bismark"
SAMTOOLS_PATH="/ye/netapp/jimmie.ye/tools/samtools-1.3"
TRIMGALORE_PATH="/ye/zaitlenlabstore/christacaggiano/trim-galore/TrimGalore-0.4.3"
BOWTIE_PATH="/ye/zaitlenlabstore/christacaggiano/bowtie2-2.3.3"

################ experiment directories ######################
input="/ye/zaitlenlabstore/christacaggiano/cfDNA_project/second_primary_methylation_data_ALS/fastq_files/zaitlenn-"$SGE_TASK_ID"_BC"
output="/zaitlen/netapp/group/christa"
fastq_prefix=$SGE_TASK_ID
scripts="scripts"

################# runs the pipeline ##########################
python wgbs.py $input $output $fastq_prefix $scripts
