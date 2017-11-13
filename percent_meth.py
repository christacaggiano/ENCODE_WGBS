
# calculating percent methylated sites
# author <arya@aryaboudaie.com>
# author <christa.caggiano@ucsf.edu>
from __future__ import print_function, division
from collections import defaultdict
import glob
import argparse

 

def run(input_file, output_file):
    i = 0
    d = defaultdict(lambda: [0,0])
    with open(input_file) as f:
        for line in f:
            if i == 0:
                i += 1
                continue
            line_split = line.split()
            key = line_split[2]+"|"+line_split[3]]

            sign = line_split[1]
            if sign == "+":
                d[key][0]+=1
            else:
                d[key][1] += 1
            i += 1
    with open(output_file, "w") as out:
        for key, value in d.items():
            chrom, site = key.split("|")
            print("{} {} {} {} {}".format(chrom, site, value[0], value[1], value[0] + value[1], value[0]/(value[0]+value[1])*100, "+"), file=out)



if __name__ == "__main__":


    parser = argparse.ArgumentParser()

    parser.add_argument("file_name", type=int, help="fastq file for processing")
    args = parser.parse_args()
    file_name = args.file_name
    
    f = open("prefixes.txt", "r")

    file_list = []
    i = 0
    name = ""
    for line in f: 
        if i<file_name:
            i+=1
        else:
            name = line.rstrip()
            break


    fn = name + "/unsortedButMerged_ForBismark_file/methylation_extraction/CpG_context_" + name + "_unsorted_merged.deduplicated.txt"
    run(fn, fn.split("/CpG_context_SRR")[0]+"/results_{}.txt".format(name))

