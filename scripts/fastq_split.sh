#!/bin/bash

INPUT_DIR=$1 
OUTPUT_DIR=$2 
LIB=$3

echo "Splitting of fastq"	

for file in $(ls $INPUT_DIR/$LIB*fastq.gz); do	
		echo $file	
		SPLIT_NAME=$( basename $file | sed 's/fastq.gz//')
		zcat $file | split -l 72000000 -d - $OUTPUT_DIR/$LIB/$SPLIT_NAME
done


