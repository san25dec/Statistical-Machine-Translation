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

def interpolateProb(sentence, uni, bi, tri):
    alpha = 0.6
    beta = 0.3
    gamma = 0.1
    prob = 1
    eps = 0.000001
    
    sent = sentence
    #sent = sentence.split()
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

def translate(sentence, translationMatrix, englishDict, frenchDict, uni, bi, tri, slopeParam, sigmaParam):
    
    frSent = sentence.split()
    enLen = int(nrand.normal(len(frSent)/slopeParam, sigmaParam))
    
    enSent = []

    prob = 1

    for i in range(enLen):

        ai = int(nrand.uniform(0, len(frSent)))
        currFr = frSent[ai]
        currFrInd = frenchDict[currFr]

        maxProb = 0
        maxInd = 0

        for j in range(len(translationMatrix)):
            if translationMatrix[j][currFrInd] > maxProb:
                maxProb = translationMatrix[j][currFrInd]
                maxInd = j
        
        for j in englishDict:
            if englishDict[j] == maxInd:
                enSent.append(j)
                break
    
        prob *= maxProb

    prob *= interpolateProb(enSent, uni, bi, tri)
    temp = ''
    for k in enSent:
        temp = temp + k + ' '

    enSent = temp
    return {'translation':enSent, 'probability':prob} 

with open('../CleanedEnglish1000.txt', 'r') as fp1:
    with open('../CleanedFrench1000.txt', 'r') as fp2:

        for c in range(7):
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

