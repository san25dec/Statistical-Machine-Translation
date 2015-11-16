import pickle
import numpy as np
from collections import Counter
from copy import deepcopy
import re
import pdb

totalSteps = 2
eng_dict = pickle.load(open("../englishDict.dict",'r'))
french_dict = pickle.load(open("../frenchDict.dict",'r'))
eng_sent = [];
french_sent = [];
with open("../CleanedFrench1000.txt", "r") as fp:
	for x in fp:
	    xTemp = re.sub('[\n]', '', x)
            words = xTemp.split()
            french_sent.append(words)
        	
with open("../CleanedEnglish1000.txt", "r") as fp:
	for x in fp:
	    xTemp = re.sub('[\n]', '', x)
            words = xTemp.split()
            eng_sent.append(words)

count_matrix = np.zeros((len(eng_dict),len(french_dict)))*(1.0/(len(eng_dict)*len(french_dict)));
translation_matrix = np.ones((len(eng_dict),len(french_dict)))*(1.0/(len(eng_dict)*len(french_dict)));
lambda_norm = np.zeros((len(eng_dict)))

for step in range(totalSteps):
	# Updating counts 

	for i in range(len(eng_sent)):
                #pdb.set_trace()
		unique_eng = Counter(eng_sent[i])
		unique_french = Counter(french_sent[i])
		sum_norm = {};
	        
                for k in unique_french:
                    sum_norm[k] = 0

		for k in unique_french:
		    for j in unique_eng:
		        sum_norm[k]+=translation_matrix[eng_dict[j]][french_dict[k]]*unique_eng[j];

		for j in unique_eng:
		    for k in unique_french:
		        count_matrix[eng_dict[j]][french_dict[k]]+=((unique_eng[j]*unique_french[k])*translation_matrix[eng_dict[j]][french_dict[k]]/sum_norm[k])
	# Updating t

        for englishWord in eng_dict:
		temp = 0
		for frenchWord in french_dict:
	#    	for index in range(len(eng_sent)):
	#    		if englishWord in eng_sent[index] and frenchWord in french_sent[index]:
			temp += count_matrix[eng_dict[englishWord]][french_dict[frenchWord]]
	        
                #pdb.set_trace()
                lambda_norm[eng_dict[englishWord]] = temp
		for frenchWord in french_dict:
        		translation_matrix[eng_dict[englishWord]][french_dict[frenchWord]] = (count_matrix[eng_dict[englishWord]][french_dict[frenchWord]])/temp

               
with open("../translationMatrix.txt", "w") as fp:
	for i in range(len(translation_matrix)):
		for j in range(len(translation_matrix[i])):
			print >> fp, translation_matrix[i][j],
		print >> fp

