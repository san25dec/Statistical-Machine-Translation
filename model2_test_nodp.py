import pickle
import numpy as np
import re
import pdb
import numpy.random as nrand
import nltk
import model2_helpers as hp

print('************** Testing IBM model 2 ***************')

tri = pickle.load(open('../trigramEnglish100.dict', 'r'))
bi = pickle.load(open('../bigramEnglish100.dict', 'r'))
uni = pickle.load(open('../unigramEnglish100.dict', 'r'))
englishDict = pickle.load(open('../englishDict100.dict', 'r'))
frenchDict = pickle.load(open('../frenchDict100.dict', 'r'))
alignmentMatrix = pickle.load(open('../alignmentMatrix100_50iter.txt', 'r'))

#translationMatrix = []

print('=====> Read files')

with open('../FitParams100.txt', 'r') as fp:
    line = fp.readline()
    line = re.sub('[\n]', '', line)
    slopeParam = float(line)

    line = fp.readline()
    line = re.sub('[\n]', '', line)
    sigmaParam = 2#float(line)

print('=====> Reading translation matrix')

translationMatrix = np.zeros((len(englishDict), len(frenchDict)))

with open('../translationMatrix100_model2_50iter.txt', 'r') as fp:
    for i in range(len(englishDict)):     
        line = fp.readline()
        
        #pdb.set_trace()
        line = re.sub('[\n]', '', line)
        vals = line.split()
        for j in range(len(frenchDict)):
            translationMatrix[i,j] = float(vals[j])
        #translationMatrix.append([float(j) for j in vals])
        #translationMatrix.append(map(float, vals))

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
    #enLen = int(nrand.normal(len(frSent)/slopeParam, sigmaParam))
    enLen = len(frSent)

    enSent = []
    
    dp_mat = []

    prob = 1
    
    # creating inverse dictionary
    inv_eng = {}
    for j in englishDict:
        inv_eng[englishDict[j]] = j
        
    # creating top indices
    
    #### To be run once for creating the top 10 index list
    
    #'''
    
    index_list = []
    for i in range(len(frenchDict)):
        tmplist = []
        tmpindex = []
        for j in range(len(englishDict)):
            tmplist.append(translationMatrix[j][i])
        tmpindex = sorted(range(len(tmplist)),key=lambda k:tmplist[k],reverse=True)
        tmplist2 = []
        for j in range(20):
            tmplist2.append(tmpindex[j])
        index_list.append(tmplist2)
    pickle.dump(index_list, open('../top20_index_100.list', 'wb'))
    
    #''' and 0
    
    ####
    
    
    
    top_index = pickle.load(open('../top20_index_100.list', 'r'))
    
    ## Alignment model
    mTemp = len(frSent)
    lTemp = enLen
    alignmentMatrix_curr = alignmentMatrix[hp.alignmentMapping(mTemp, lTemp)][0:lTemp, 0:mTemp]
    translatedSentence = ''
    for i in range(enLen):
    
        ai = i#np.argmax(alignmentMatrix_curr[i, 0:mTemp])#int(nrand.uniform(0, len(frSent)))
        currFr = frSent[ai]
        currFrInd = frenchDict[currFr]
        currEnInd = np.argmax(translationMatrix[0:len(translationMatrix[0]), currFrInd])
        translatedSentence += ' ' + inv_eng[currEnInd]
        maxprob = translationMatrix[currEnInd][currFrInd]
        #maxProb = 0
        #maxInd = 0 
        #template_entry = []
        
        '''
	if i==0:
	    for j in range(len(translationMatrix)):
	        template_entry.append((inv_eng[j],translationMatrix[j][currFrInd]*lang_model_scores(inv_eng[j],'',uni,bi,1)))
            dp_mat.append(template_entry)
        else:
            for j in range(len(translationMatrix)):
                maxval = 0
                for k in range(len(top_index[0])):
                    currEngInd = top_index[currFrInd][k]
                    probtemp = translationMatrix[currEngInd][currFrInd]*lang_model_scores(inv_eng[currEngInd],dp_mat[i-1][j][0],uni,bi,2)
                    if maxval<probtemp:
                        maxval = probtemp
                        maxword = inv_eng[currEngInd]
                template_entry.append((maxword,maxval))
            dp_mat.append(template_entry)
        ''' and 0
    #translated_sent = ''  
    #maxprob = 0
    
    #print(dp_mat)
    '''
    for i in range(len(translationMatrix)):
        tmp_sent = ''
        tmp_prob = 1
        
        for j in range(enLen):
            tmp_sent = tmp_sent+dp_mat[j][i][0]+' '
            tmp_prob = tmp_prob*dp_mat[j][i][1]
            
        if maxprob<=tmp_prob:    
            maxprob = tmp_prob
            translated_sent = tmp_sent
    #print('** Max prob :')
    #print(maxprob)
    ''' and 0
    return {'translation':translatedSentence, 'probability':maxprob} 
    
with open('../CleanedEnglish100.txt', 'r') as fp1:
    with open('../CleanedFrench100.txt', 'r') as fp2:

        for num in range(0,5):
            frSent = fp2.readline()
            enSent = fp1.readline()

            frSent = re.sub('[\n]', '', frSent)
            enSent = re.sub('[\n]', '', enSent)
            print('=====> Read french Sentence')
            print('=====> Translating to english')
            out = translate(frSent, translationMatrix, englishDict, frenchDict, uni, bi, tri, slopeParam, sigmaParam)
            print('=====> Finished translation')
            print('==================================')
            print 'French Sentence: ', frSent
            print('----------------------------------')
            print 'English Sentence: ', enSent
            print('----------------------------------')
            print 'Translated Sentence: ', out['translation']
            print('----------------------------------')

            ## Computing bleu score
            print 'BLEU score of translation', nltk.bleu(out['translation'],[enSent, enSent, enSent],[0.25, 0.25, 0.25, 0.25])
            print('==================================')
