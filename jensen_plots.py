import pandas as pd
import glob
from collections import defaultdict, Counter
from math import isnan
from numpy import nan
import progressbar
import pickle


def get_files(name): 
	return glob.glob(name)

def get_prefix(file): 
	return file.split("/")[0]

def srr_path(srr_name):
	return str(srr_name)+"/unsortedButMerged_ForBismark_file/methylation_extraction/results_new.txt"

if __name__=="__main__":	
	key = pd.read_csv("jensen_key_plaintext.csv", delimiter="\t") 
	categories = list(key)

	key_list = {key:[] for key in categories}
	for column in key: 
		key_list[column] = list(key[column])

	#print(key_list)

	#file_list = get_files("SRR*/unsortedButMerged_ForBismark_file/methylation_extraction/results_new.txt") 
	#prefixes = get_prefix(file_list)

	results_by_key = {key:Counter() for key in categories}
	

	#print(results_by_key)
	for key, results in key_list.items():
		bar = progressbar.ProgressBar()
		for srr in bar(results):
			if srr==nan or srr=="SRR1759726": continue
			results_file = srr_path(srr)
			try:
				df = pd.read_csv(results_file, delimiter=" ", header=None)
			except Exception as e:
				continue
			ser = df[4].apply(lambda x: int(x*100)) # round the last column to two places
			results_by_key[key]+=Counter(ser)
	print(results_by_key)
#	percents_by_key = {}
#	for key, counts in results_by_key.items():
#		total = sum(counts.values())
#		percents = [counts[x]/total for x in range(100+1)]
#
#		percents_by_key[key] = percents
#	print(percents_by_key)
#	with open("percents.pickle", "w") as pf:
#		pickle.dump(percents_by_key, pf)
#	with open("results.pickle", "w") as pf:
#		pickle.dump(results_by_key, pf)
	

#	dictionary where pregnant --> list of all the values
#	of the results_new that map to that category 
	
	f.open("results.pkl", "wb")
	pickle.dump(results_by_key, f)
	f.close()



