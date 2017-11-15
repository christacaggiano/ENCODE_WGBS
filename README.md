# ENCODE WGBS PIPELINE 

End to end implementation of the [ENCODE](https://www.encodeproject.org/) whole genome bisulfite sequencing pipeline described [here](https://www.encodeproject.org/wgbs/). 
Builds off [DNANexus](https://wiki.dnanexus.com/Home) WGBS framework and work from the [Myers lab at the HudsonAlpha Institute for Biotechnology](http://research.hudsonalpha.org/Myers/?page_id=660)

## Overview
------ 
Takes raw whole-genome bisulfite sequencing data (fastq files) and returns the number of methylated CpGs found at each site. Performs preliminary methylation analysis based on [MethylKit](https://github.com/al2na/methylKit). 

## Requirements
------

(1) Bowtie 2 read aligner 

[Bowtie 2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml) - used to align raw fastq reads to a genome of choice 

(2) 


Bisulfite converted genome 

Used by bismark for alignment. 

