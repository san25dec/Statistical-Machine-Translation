import pickle
import numpy as np
from collections import Counter
from copy import deepcopy


eng_dict = pickle.load()
french_dict = pickle.load()
sentences = pickle.load()

eng_sent = sentences['english'];
french_sent = sentences['french'];

count_matrix = np.ones((len(eng_dict),len(french_dict)))*(1.0/(len(eng_dict)*len(french_dict)));
translation_matrix = np.ones((len(eng_dict),len(french_dict)))*(1.0/(len(eng_dict)*len(french_dict)));

lambda_norm = deepcopy(eng_dict);
lambda_norm = dict.fromkeys(lambda_norm,0)

# Updating counts 

for i in range(len(eng_sent)):
    unique_eng = Counter(eng_sent[i])
    unique_french = Counter(french_sent[i])
    sum_norm = [0]*len(unique_french);
    
    for k in range(len(unique_french)):
        for j in range(len(unique_eng)):
            sum_norm[k]+=translation_matrix[unique_eng[j][0]][unique_french[k][0]];    
    labmda_norm = 0;
    for j in range(len(unique_eng)):
        for k in range(len(unique_french)):
            count_matrix[eng_dict[eng_sent[i][j]]][french_dict[french_sent[i][k]]]+=unique_eng[j][1]*unique_french[k][1];
            count_matrix[eng_dict[eng_sent[i][j]]][french_dict[french_sent[i][k]]]*=translation_matrix[eng_dict[eng_sent[i][j]]][french_dict[french_sent[i][k]]]/sum_norm[k];
    	    lambda_norm[eng_dict[eng_sent[i][j]]] = lambda_norm[eng_dict[eng_sent[i][j]]]+count_matrix[eng_dict[eng_sent[i][j]]][french_dict[french_sent[i][k]]];
    	    
# Updating t

           
        
            



