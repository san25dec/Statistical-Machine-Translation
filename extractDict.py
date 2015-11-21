import re
import pickle

frenchSet = set()
englishSet = set()
frenchDict = {}
englishDict = {}

with open('../CleanedFrench10000.txt', 'r') as rFr:
    for x in rFr:
        xTemp = re.sub('[\n]', '', x)
        words = xTemp.split()
        
        for word in words:
            frenchSet.add(word)
        
with open('../CleanedEnglish10000.txt', 'r') as rEn:
    for x in rEn:
        xTemp = re.sub('[\n]', '', x)
        words = xTemp.split()

        for word in words:
            englishSet.add(word)
        
i = 0
j = 0
for word in frenchSet:
    frenchDict[word] = i
    i += 1

for word in englishSet:
    englishDict[word] = j
    j += 1

print(len(englishSet))
pickle.dump(frenchDict, open('../frenchDict.dict', 'wb'))
pickle.dump(englishDict, open('../englishDict.dict', 'wb'))

