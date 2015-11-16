import re

Sentences = {}


with open('../europarl-v7.fr-en.fr', 'r') as fFr:
    with open('../CleanedFrench.txt', 'wb') as wFr:
        for x in fFr:
            xTemp = x.lower()
            xTemp = re.sub('[\\\\?".:\-();/%#+@!&*={}\n]', "", xTemp)
            xTemp = re.sub("[']", "", xTemp) 
            xTemp = re.sub("[,]", " ", xTemp)
            wFr.write(xTemp)
            wFr.write("\n")
            #sentence = re.split(',|\t| ', xTemp)
            #sentence = filter(None, sentence)

with open('../europarl-v7.fr-en.en', 'r') as fEn:
    with open('../CleanedEnglish.txt', 'wb') as wEn:
        for x in fEn:
            xTemp = x.lower()
            xTemp = re.sub('[\\\\?".:\-();/%#+@!&*={}\n]', "", xTemp)
            xTemp = re.sub("[']", "", xTemp) 
            #sentence = re.split(',|\t| ', xTemp)
            #sentence = filter(None, sentence)
            xTemp = re.sub("[,]", " ", xTemp)
            wEn.write(xTemp)
            wEn.write("\n")
