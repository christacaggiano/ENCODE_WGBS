
# calculating percent methylated sites
# author <christa.caggiano@ucsf.edu>
# author <aryab@google.com>
from __future__ import print_function, division
from collections import defaultdict
import glob
import argparse

 
 # glob.glob("SRR*/unsortedButMerged_ForBismark_file/methylation_extraction/CpG_context_SRR*_unsorted_merged.deduplicated.txt")
def write_results(key, value, output_file):
    with open(output_file, "a") as out:
        print(str(key[0]) + str(key[1]) + str(value[0]) + str(value[1]) + str(value[0]/(value[0]+value[1])), file=out)

def run(input_file, output_file):
    i = 0
    previous_key = []
    pluses = 0
    minuses = 0
    with open(input_file) as f:
        for line in f:
            if i == 0:
                i += 1
                continue
            line_split = line.split()
            key = [line_split[2], line_split[3]]
            if previous_key and key != previous_key:
                write_results(previous_key, [pluses, minuses], output_file)
                pluses = 0
                minuses = 0

            previous_key = key

            sign = line_split[1]
            if sign == "+":
                pluses += 1
            else:
                minuses += 1
            i += 1



if __name__ == "__main__":


    parser = argparse.ArgumentParser()

    parser.add_argument("file_name", type=int, help="fastq file for processing")
    args = parser.parse_args()
    file_name = args.file_name
    
    f = open("prefixes.txt", "r")

    file_list = []
    for line in f: 
        file_list.append(line.rstrip())

    name = file_list[file_name]


    fn = name + "/unsortedButMerged_ForBismark_file/methylation_extraction/CpG_context_" + name + "_unsorted_merged.deduplicated.txt"
    run(fn, fn.split("/CpG_context_SRR")[0]+"/results.txt")

