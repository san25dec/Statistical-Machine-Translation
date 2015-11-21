import re

Sentences = {}


with open('fr-en/europarl-v7.fr-en_1000.fr', 'r') as fFr:
    with open('fr-en/CleanedFrench.txt', 'wb') as wFr:
        for x in fFr:
            xTemp = x.lower()
            xTemp = re.sub('[\\\\?".:\-();/%#+@!&*={}\n]', "", xTemp)
            xTemp = re.sub("[']", "", xTemp) 
            xTemp = re.sub("[,]", " ", xTemp)
            wFr.write(xTemp)
            wFr.write("\n")
            #sentence = re.split(',|\t| ', xTemp)
            #sentence = filter(None, sentence)

with open('fr-en/europarl-v7.fr-en_1000.en', 'r') as fEn:
    with open('fr-en/CleanedEnglish.txt', 'wb') as wEn:
        for x in fEn:
            xTemp = x.lower()
            xTemp = re.sub('[\\\\?".:\-();/%#+@!&*={}\n]', "", xTemp)
            xTemp = re.sub("[']", "", xTemp) 
            #sentence = re.split(',|\t| ', xTemp)
            #sentence = filter(None, sentence)
            xTemp = re.sub("[,]", " ", xTemp)
            wEn.write(xTemp)
            wEn.write("\n")
