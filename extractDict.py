import re
import pickle

frenchSet = set()
englishSet = set()
frenchDict = {}
englishDict = {}

with open('../CleanedFrench10.txt', 'r') as rFr:
    for x in rFr:
        xTemp = re.sub('[\n]', '', x)
        words = xTemp.split()
        
        for word in words:
            frenchSet.add(word)
        
with open('../CleanedEnglish10.txt', 'r') as rEn:
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

#Adding the null to the dictionary
#englishDict['xxnullxx'] = j

print(len(englishSet))
pickle.dump(frenchDict, open('../frenchDict10.dict', 'wb'))
pickle.dump(englishDict, open('../englishDict10.dict', 'wb'))

