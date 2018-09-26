#!/bin/sh

INPUT_DIR=$1
OUTPUT_DIR=$2
PREFIX=$3

echo "Splitting of fastq"       

for file in $(ls $INPUT_DIR/$PREFIX*fq.gz); do
                echo $file      
                SPLIT_NAME=$( basename $file | sed 's/fq.gz//')
                zcat $file | split -l 72000000 -d - $OUTPUT_DIR/$PREFIX/$SPLIT_NAME
done
