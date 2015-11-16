import re
import pickle

frenchDict = {}

with open('../CleanedFrench.txt', 'r') as rFr:
    for x in rFr:
        xTemp = re.sub('[\n]', '', x)
        words = xTemp.split()
        
        for word in words:
            if word in frenchDict
