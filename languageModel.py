import pickle
def sentenceProb(line, triprob, biprob, uniprob, l3, l2, l1, l0):
	splitline = line.split(" ")
	value = 1
	for i in range(len(splitline)):
		temp = 0
		if i >= 2:
			tup = (splitline[i-1], splitline[i-2])
			if tup in triprob:
				temp = l3 * triprob[tup]
		if i >= 1:
			tup = splitline[i-1]
			if tup in biprob:
				temp += l2 * biprob[tup]
		tup = splitline[i]
		if tup in uniprob:
			temp += l1 * uniprob[tup]
		temp += l0 / 1000
		value *= temp
	return value