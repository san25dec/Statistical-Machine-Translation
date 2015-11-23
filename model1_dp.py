import pickle
import numpy as np
import re
import pdb
import numpy.random as nrand

print('************** Testing IBM model 1 ***************')

tri = pickle.load(open('../trigramEnglish1000.dict', 'r'))
bi = pickle.load(open('../bigramEnglish1000.dict', 'r'))
uni = pickle.load(open('../unigramEnglish1000.dict', 'r'))
englishDict = pickle.load(open('../englishDict.dict', 'r'))
frenchDict = pickle.load(open('../frenchDict.dict', 'r'))
translationMatrix = []

print('=====> Read files')

with open('../FitParams.txt', 'r') as fp:
    line = fp.readline()
    line = re.sub('[\n]', '', line)
    slopeParam = float(line)

    line = fp.readline()
    line = re.sub('[\n]', '', line)
    sigmaParam = float(line)

print('=====> Reading translation matrix')

with open('../translationMatrix.txt', 'r') as fp:
    for i in range(len(englishDict)):     
        line = fp.readline()
        
        #pdb.set_trace()
        line = re.sub('[\n]', '', line)
        vals = line.split()
        
        #translationMatrix.append([float(j) for j in vals])
        translationMatrix.append(map(float, vals))

#pdb.set_trace()


def lang_model_scores(word1,word2,uni,bi,flag):
    
    alpha = 0.5
    beta = 0.5
    eps = 0.0001
    
    if flag == 1:
        if word1 in uni:
            return alpha*uni[word1]
        else:
            return eps
    else:
        if word1 in bi and word2 in bi[word1]:
            return beta*bi[word1][word2]
        else:
            return eps
        
        
    
# sub-optimal translation

def translate(sentence, translationMatrix, englishDict, frenchDict, uni, bi, tri, slopeParam, sigmaParam):
    
    frSent = sentence.split()
    enLen = int(nrand.normal(len(frSent)/slopeParam, sigmaParam))
    
    enSent = []
    
    dp_mat = []

    prob = 1
    
    # creating inverse dictionary
    inv_eng = {}
    for j in englishDict:
        inv_eng[englishDict[j]] = j
    
    for i in range(enLen):

        ai = int(nrand.uniform(0, len(frSent)))
        currFr = frSent[ai]
        currFrInd = frenchDict[currFr]

        maxProb = 0
        maxInd = 0 
        template_entry = []
        
	
	if i==0:
	    for j in range(len(translationMatrix)):
	        template_entry.append((inv_eng[j],translationMatrix[j][currFrInd]*lang_model_scores(inv_eng[j],'',uni,bi,1)))
            dp_mat.append(template_entry)
        else:
            for j in range(len(translationMatrix)):
                maxval = 0
                for k in range(len(translationMatrix)):
                    probtemp = translationMatrix[k][currFrInd]*lang_model_scores(inv_eng[k],dp_mat[i-1][j][0],uni,bi,2)
                    if maxval<probtemp:
                        maxval = probtemp
                        maxword = inv_eng[k]
                template_entry.append((maxword,maxval))
            dp_mat.append(template_entry)
    
    translated_sent = ''  
    maxprob = 0        
    #print(dp_mat)
    
    for i in range(len(translationMatrix)):
        tmp_sent = ''
        tmp_prob = 1
        
        for j in range(enLen):
            tmp_sent = tmp_sent+dp_mat[j][i][0]+' '
            tmp_prob = tmp_prob*dp_mat[j][i][1]
            
        if maxprob<=tmp_prob:    
            maxprob = tmp_prob
            translated_sent = tmp_sent
    print('** Max prob :')
    print(maxprob)
    return {'translation':translated_sent, 'probability':maxprob} 

with open('../CleanedEnglish1000.txt', 'r') as fp1:
    with open('../CleanedFrench1000.txt', 'r') as fp2:

        frSent = fp2.readline()
        enSent = fp1.readline()
        frSent = fp2.readline()
        enSent = fp1.readline()

        frSent = re.sub('[\n]', '', frSent)
        enSent = re.sub('[\n]', '', enSent)
        print('=====> Read french Sentence')
        print('=====> Translating to english')
        out = translate(frSent, translationMatrix, englishDict, frenchDict, uni, bi, tri, slopeParam, sigmaParam)
        print('=====> Finished translation')
        print 'French Sentence: ', frSent
        print 'English Sentence: ', enSent
        print 'Translated Sentence: ', out['translation']

