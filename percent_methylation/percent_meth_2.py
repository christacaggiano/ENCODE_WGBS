from __future__ import print_function, division
from collections import defaultdict
import argparse 
import os 
import glob 
import os.path

def add_to_file(file, lines): 
    with open(file , "a") as out:
        for chrom, site, ratio in lines:
            print("{} {} {} {} {} {} {}".format(chrom, site, ratio[0], ratio[1], ratio[0] + ratio[1], ratio[0]/(ratio[0]+ratio[1])*100, "+"), file=out)

if __name__ == "__main__":

    # parser = argparse.ArgumentParser()

    # parser.add_argument("file_name", type=int, help="fastq file for processing")
    # args = parser.parse_args()
    # file_name = args.file_name
    
    # prefix = open("prefixes.txt", "r")

    # file_list = []
    # for line in prefix: 
    #     file_list.append(line.rstrip())
    # name = file_list[file_name]

    # os.chdir(name + "/unsortedButMerged_ForBismark_file/methylation_extraction/")

    categories = ["Placenta", "Pregnant.ccfDNA", "Buffy.Coat", "NonPregnant.ccfDNA"]
    file_list = []
    for category in categories:
        file_list += glob.glob(category + "/" + category + "*.txt")
    

    lines = []

    ratio = [0,0]
    prev_key = ""

    
    for file in file_list: 
        no_ext = file.split(".txt")[0]
        try:
            os.remove("{}_merged.txt".format(no_ext))
        except:
            pass
        os.system("touch {}_merged.txt".format(no_ext))
        sorted_fname = no_ext+"_sorted.txt"
        if not os.path.isfile(sorted_fname):
            os.system("sort {} > {}".format(file, sorted_fname))


        with open(sorted_fname) as f:
            first = True

            for line in (f):
                line_split = line.split()
                if len(line_split)==1: 
                    continue
                else:
                    key = line_split[0]+"|"+line_split[1]
                    if not first and key!=prev_key:
                        lines.append([line_split[0], line_split[1], ratio])
                        if len(lines)==500:
                            add_to_file(no_ext+"_merged.txt", lines)
                            lines=[]
                        ratio = [0,0]
                    prev_key = key
                    ratio[0]+=int(line_split[2])
                    ratio[1]+=int(line_split[3])
                    first = False
            add_to_file(no_ext+"_merged.txt", lines)
            lines = []
            ratio = [0,0]

        