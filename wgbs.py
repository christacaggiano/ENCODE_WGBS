
# Python implementation of ENCODE WGBS pipeline 
# uses bash scripts from https://github.com/ENCODE-DCC/dna-me-pipeline
# 29 Sept 2017, Zaitlen Laboratory 
# author <christa.caggiano@ucsf.edu> 

import argparse
import subprocess
import os


def make_directories(dir_path): 
    if not(os.path.exists(dir_path)):
            os.mkdir(dir_path)


def get_fastq(dir_path): 

    fastq1 = []
    fastq2 = []

    for fastq in os.listdir(dir_path): 
        if name in fastq and "_1" in fastq: 
            fastq1.append(fastq)
            fastq2.append(fastq.replace("_1","_2"))

    return fastq1, fastq2


def run_split_file(input_dir, output): 

    split_file_cmd = "./fastq_split.sh" + " " + input_dir + " " + output

    # split fastq files into groups of 18 million reads
    subprocess.call(split_file_cmd, shell=True)


def run_bismark(dir_path): 

    bam_path = dir_path + "/bam_files"
    log_path = dir_path + "/log_path"
    temp_dir = dir_path + "/temp_dir"

    make_directories(bam_path) 
    make_directories(log_path)
    make_directories(temp_dir)

    fastq1, fastq2 = get_fastq(dir_path)

    for i in range(len(fastq1)): 
        bismark_cmd = "./trim_galore_bismark_alignment.sh" + " " + fastq1[i] + " " + fastq2[i] + " " + bam_path + " " + temp_dir
        subprocess.call(bismark_cmd, shell=True)


def run_merge_call_methylation(dir_path): 

    bam_path = dir_path + "/bam_files"

    merge_cmd = "mergeUnsorted_dedup_files_for_methExtraction_orig.sh" + " " + dir_path + " " + str(name)
    subprocess.call(merge_cmd)


if __name__=="__main__":

    # takes in command line arguments
    # @TODO make run/output optional 

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="path containing fastq files")
    parser.add_argument("output", help="path where outputdir should be created")
    parser.add_argument("file_name", nargs="+", help="fastq file for processing")
    args = parser.parse_args()
    
    output = args.output
    file_name = args.file_name
    input_dir = args.input 

    make_directories(output)

    for name in file_name: 

        print("splitting files for" + str(name))
        # run_split_file(input_dir + "/" + name, output)
        print("done splitting files") 
        print()
        print()


        dir_path = output + "/" + name 
        make_directories(dir_path) 
        print("Trimming and running bismark for " + str(name)) 
        run_bismark(dir_path)
        print("done running bismark")
        print()
        print()

        print("calling methylation for " + str(name))
        run_merge_call_methylation(dir_path, name)
        print("done calling methylation")
        print()
        print()

    print("Finished.") 





