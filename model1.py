import pickle
import numpy as np
from collections import Counter
from copy import deepcopy

totalSteps = 10
eng_dict = pickle.load("englishDict.dict")
french_dict = pickle.load("frenchDict.dict")
eng_sent = [];
french_sent = [];
with open("../CleanedFrench.txt", "r") as fp:
	for x in fp:
		xTemp = re.sub('[\n]', '', x)
        words = xTemp.split()
        french_sent.append(words)
        	
with open("../CleanedEnglish.txt", "r") as fp:
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
		unique_eng = Counter(eng_sent[i])
		unique_french = Counter(french_sent[i])
		sum_norm = [0]*len(unique_french);
		
		for k in range(len(unique_french)):
		    for j in range(len(unique_eng)):
		        sum_norm[k]+=translation_matrix[unique_eng[j][0]][unique_french[k][0]];    
		for j in range(len(unique_eng)):
		    for k in range(len(unique_french)):
		        count_matrix[eng_dict[eng_sent[i][j]]][french_dict[french_sent[i][k]]]+=((unique_eng[j][1]*unique_french[k][1])*(translation_matrix[eng_dict[eng_sent[i][j]]][french_dict[french_sent[i][k]]]/sum_norm[k]))

			    
	# Updating t



	for englishWord in eng_dict:
		temp = 0
		for frenchWord in french_dict:
	#    	for index in range(len(eng_sent)):
	#    		if englishWord in eng_sent[index] and frenchWord in french_sent[index]:
			temp += count_matrix[eng_dict[englishWord]][french_dict[frenchWord]]
		lambda_norm[eng_dict[englishWord]] = temp
		for frenchWord in french_dict:
			translation_matrix[eng_dict[englishWord]][french_dict[frenchWord]] = (count_matrix[eng_dict[englishWord]][french_dict[frenchWord]])/temp

with open("translationMatrix.txt", "w") as fp:
	for i in range(len(translation_matrix)):
		for j in range(len(translation_matrix[i])):
			print >> fp, translation_matrix[i][j],
		print >> fp

