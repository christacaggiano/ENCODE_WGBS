import os 

def file_list(prefixes): 
	file_list = []
	for p in prefixes: 
		loc = "/ye/zaitlenlabstore/christacaggiano/dna-me-pipeline/HAIB/bismark_pipeline/" + p + "/unsortedButMerged_ForBismark_file/methylation_extraction"
		file_list.append(loc + "/results_new.txt")
	return file_list

def concat(file_list, category, number): 

	input_string = "cat " + " ".join(file_list) + " > " + category + "_" + str(number) + ".txt"

	if not os.path.exists(category): os.mkdir(category)
	os.chdir(category)
	os.system(input_string)
	os.chdir("/ye/zaitlenlabstore/christacaggiano/dna-me-pipeline/HAIB/bismark_pipeline")

if __name__ == "__main__": 

	with open("jensen_key_plaintext_transpose.txt", "r") as f:  
		
		category = "" 

		for line in f:  
			
			if not line.split()[0] == category: 
				individual_number = 0 
			else: 
				individual_number += 1 
			
			individual = line.split() 
			category = individual[0]
			prefixes = individual[1:]
			concat((file_list(prefixes)), category, individual_number)
			 