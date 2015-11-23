# Helps obtaining the category to which this sentence lies in
# l refers to the length of the sentence
# There are 8 categories of length
import pdb
import numpy as np

def categoryFn(l):
    cat = 0
    if l <= 5 and l > 0:
        cat = 0
    elif l <= 10:
        cat = 1
    elif l <= 15:
        cat = 2
    elif l <= 20:
        cat = 3
    elif l <= 25:
        cat = 4
    elif l <= 30:
        cat = 5
    elif l <= 35:
        cat = 6
    elif l <= 40:
        cat = 7
    elif l <= 45:
        cat = 8
    elif l <= 50:
        cat = 9
    elif l <= 55:
        cat = 10
    else:
        cat = 11
    return cat

# Given the length of the French(m) and English(l) sentence
# It gives the dictionary key for accessing the alignmentMatrix

def alignmentMapping(m, l):
    return (categoryFn(m), categoryFn(l))

def createAlignmentMatrix():
    alignment_matrix = {}
    for i in range(12):
        for j in range(12):

            if i < 11 and j < 11:
                alignment_matrix[(j,i)] = np.zeros(((i+1)*5,(j+1)*5))
            elif i < 11 and j == 11:
                alignment_matrix[(j,i)] = np.zeros(((i+1)*5,120))
            elif i == 11 and j < 11:
                alignment_matrix[(j,i)] = np.zeros((120,(i+1)*5))
            else:
                alignment_matrix[(j,i)] = np.zeros((120,120))

    return alignment_matrix

def createMuMatrix():
    
    mu_matrix = {}
    for i in range(12):
        for j in range(12):

            if j < 11:
                mu_matrix[(j,i)] = np.zeros((j+1)*5)
            else:
                mu_matrix[(j,i)] = np.zeros(120)
    
    return mu_matrix

# Given 2 words, it sees if they are same or not
# If they are the same, it returns 1, otherwise 0

def deltaFn(f1, f2):
    if f1 == f2:
        return 1
    else:
        return 0

def c_of_f_given_e(e, f, eng_words, french_words, eng_dict, french_dict, alignment_matrix, translation_matrix):
	
    l = len(eng_words)
    m = len(french_words)
    
    delta_f = np.zeros((1,m))
    delta_e = np.zeros((l,1))
    delta_f[0][[i for i, j in enumerate(french_words) if j == f]] = 1
    delta_e[[i for i, j in enumerate(eng_words) if j == e]] = 1
    delta_f = delta_f.repeat(l,0)
    delta_e = delta_e.repeat(m,1)
    a = alignment_matrix[alignmentMapping(m, l)][0:l,0:m]
    '''print('*****')
    print('l:%d m:%d'%(l,m))
    print(alignmentMapping(m, l))
    print(a.shape)
    print(delta_e.shape)
    print(delta_f.shape)
    print('*****')''' and 0
    #pdb.set_trace() 
    eff_prod = delta_e * delta_f * a
    t = np.array([[translation_matrix[eng_dict[w]][french_dict[f]] for w in eng_words]])
    denom = t.dot(a)
    denom = denom.repeat(l, 0)
    
    eff_prod = (1.0*eff_prod)/denom
    counts = eff_prod.sum()

    '''
    counts = 0
    for j in range(m):
        for i in range(l):
            counts_temp = translation_matrix[eng_dict[e]][french_dict[f]] * \
                          alignment_matrix[alignmentMapping(m, l)][i][j] * \
                          deltaFn(f, french_words[j]) * \
                          deltaFn(e, eng_words[i])
            norm = 0
           
            for k in range(len(eng_words)):
                norm += translation_matrix[eng_dict[eng_words[k]]][french_dict[f]] * alignment_matrix[alignmentMapping(m, l)][k][j]
        
            counts += (1.0*counts_temp) / norm
    ''' and 0
    return counts
			
"""def c_mlFE(m, l, E, F, translation_matrix, alignment_matrix, eng_dict, french_dict):
    
    count = translation_matrix[eng_dict[E[i]]][french_dict[F[j]]] * alignment_matrix[alignmentMapping(m, l)][i][j]

    t = np.array([[translation_matrix[eng_dict[w]][french_dict[F[j]]] for w in E]])
    a = alignment_matrix
    norm = 
    '''for i1 in range(len(E)):
        norm += translation_matrix[eng_dict[E[i1]]][french_dict[F[j]]] * alignment_matrix[alignmentMapping(m, l)][i1][j]
    ''' and 0
    count = (1.0*count) / norm
    
    return count
""" and 0
													
			
	
