# Python implementation of ENCODE WGBS pipeline
# uses bash scripts from https://github.com/ENCODE-DCC/dna-me-pipeline
# 29 Sept 2017, Zaitlen Laboratory
# author <christa.caggiano@ucsf.edu>

from __future__ import print_function
import argparse
import subprocess
import os


def make_directories(dir_path):
    """
    Checks if directory exists, otherwise, makes the directory
    :param dir_path: directory to be made
    :returns: NONE
    """

    if not (os.path.exists(dir_path)):
        os.mkdir(dir_path)


def get_fastq(dir_path):

    """
    finds all the relelvant paired fastq files in a directory 
    :param dir_path: directory for files to be discovered 
    :returns: list of the fwd and rv fastq file names 
    """

    fastq1 = []
    fastq2 = []

    # iterates over all the fastq files in the directory 
    # and finds appropriate pairs for paired end analysis 
    # returns list of each fastq 
    for fastq in os.listdir(dir_path): 
        if "R1" in fastq: 
            fastq1.append(fastq)
            fastq2.append(fastq.replace("R1","R2"))

    return fastq1, fastq2


def run_split_file(input_dir, output, name, script_directory):
    """
    runs split file command to split fastq into 18 milllion reads
    for further processing
    :param input_dir: dir containing files to be split
    :param output: output dir for analysis
    :param name: subdirectory for output

    """

    # calls fastq_split.sh with the input dir of file and output dir
    split_file_cmd = script_directory + "/fastq_split.sh" + " " + input_dir + " " + output + " " + name
    subprocess.call(split_file_cmd, shell=True)


def run_bismark(dir_path, script_directory):
    """
    runs trim galore and bismark
    :param dir_path: output dir path
    """

    # names and makes directories for analysis output
    bam_path = dir_path + "/bam_files"
    log_path = dir_path + "/log_path"
    temp_dir = dir_path + "/temp_dir"

    make_directories(bam_path)
    make_directories(log_path)
    make_directories(temp_dir)

    # gets list of relevant fastq files
    fastq1, fastq2 = get_fastq(dir_path, name)

    # for each fastq file pair, run trimgalore and bismark
    # this step takes a while
    for i in range(len(fastq1)):
        bismark_cmd = "./trim_galore_bismark_alignment.sh" + " " + dir_path + "/" + fastq1[i] + " " + dir_path + "/" + \
                    " " + bam_path + " " + temp_dir + " " + str(i)
        subprocess.call(bismark_cmd, shell=True)


def run_merge_call_methylation(output, dir_path, name):
    """
    runs methylation call
    :param dir_path: output dir
    :param name: name of file for analysis
    """
    bam_path = dir_path + "/bam_files"
    methy_path = dir_path + "/unsortedButMerged_ForBismark_file"
    make_directories(methy_path)

    # calls methylation extraction
    merge_cmd = "./mergeUnsorted_dedup_files_for_methExtraction.sh" + " " + dir_path + " " + bam_path + " " + name + " " + os.getcwd()

    subprocess.call(merge_cmd, shell=True)


if __name__ == "__main__":

    # takes in command line arguments for input, output, and which file to use
    # @TODO make run/output optional
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="path containing fastq files")
    parser.add_argument("output", help="path where outputdir should be created")
    parser.add_argument("file_name", type=str, help="fastq file for processing")
    parser.add_argument("script_directory", type=str, help="where bismark shell scripts live")
    args = parser.parse_args()

    output = args.output
    file_name = args.file_name
    input_dir = args.input
    script_directory = args.script_directory

    name = file_name

    make_directories(output)

    # # for each file we want to analyze, run pipeline
    print("splitting files for " + str(name))
    run_split_file(input_dir, output, name)
    print("done splitting files")

    dir_path = output + "/" + name
    make_directories(dir_path)
    print("Trimming and running bismark for " + str(name))
    run_bismark(dir_path)
    print("done running bismark")
  
    print("calling methylation for " + str(name))
    run_merge_call_methylation(output, dir_path, name)
    print("done calling methylation")

    print("Finished.")





