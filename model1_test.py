import pickle
import numpy as np
import re
import pdb

tri = pickle.load(open('../trigramEnglish10000.dict', 'r'))
bi = pickle.load(open('../bigramEnglish10000.dict', 'r'))
uni = pickle.load(open('../unigramEnglish10000.dict', 'r'))
englishDict = pickle.load(open('../englishDict.dict', 'r'))
frenchDict = pickle.load(open('../frenchDict.dict', 'r'))
translation_matrix = np.ones((len(englishDict), len(frenchDict)))

with open('../translationMatrix.txt', 'r') as fp:
    for i in range(len(translation_matrix)):     
        line = fp.readline()
        
        #pdb.set_trace()
        line = re.sub('[\n]', '', line)
        vals = line.split()
        
        #pdb.set_trace()
        for j in range(len(vals)):          
            translation_matrix[i][j] = float(vals[j])

           
#pdb.set_trace()

def interpolateProb(sentence, uni, bi, tri):
    alpha = 0.6
    beta = 0.3
    gamma = 0.1
    prob = 1
    eps = 0.000001

    sent = sentence.split()
    for j in range(0,len(sent)):
        t = 0

        if sent[j] in uni:
            t += gamma*uni[sent[j]] 
        else:
            t += gamma*eps

        if j >= 1:
            if sent[j-1] in bi and sent[j] in bi[sent[j-1]]:
                t += beta*bi[sent[j-1]][sent[j]]
            else:
                t += beta*eps

        if j >= 2:
            if (sent[j-1],sent[j-2]) in tri and sent[j] in tri[(sent[j-1],sent[j-2])]:
                t += alpha*tri[(sent[j-1],sent[j-2])][sent[j]]
            else:
                t += alpha*eps

        prob *= t

    return prob
    
with open('../CleanedEnglish10000.txt', 'r') as fp1:
    with open('../CleanedFrench10000.txt', 'r') as fp2:
        for i in range(0,10):
            lEn = fp1.readline()
            print 'Sentence: ', lEn,
            print ' Prob: ', interpolateProb(lEn, uni, bi, tri)

        lFr = fp1.readline()
        
