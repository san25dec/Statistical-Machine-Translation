import pickle
def trigram(infile, outfile):
	fp = open(infile, "r")
	data = fp.read().split()
	fp.close()
	triprob = {}
	count = {}
	for i in range(2, len(data)):
		key = (data[i-1], data[i-2])
		if key not in triprob:
			triprob[key] = {}
			count[key] = 0
		if data[i] not in triprob[key]:
			triprob[key][data[i]] = 0
		triprob[key][data[i]] += 1
		count[key] += 1
	for i in triprob:
		for j in triprob[i]:
			triprob[i][j] = triprob[i][j] / count[i]
	with open(outfile, 'wb') as f:
		pickle.dump(triprob, f)
	# print triprob

def bigram(infile, outfile):
	fp = open(infile, "r")
	data = fp.read().split()
	fp.close()
	biprob = {}
	count = {}
	for i in range(1, len(data)):
		key = data[i-1]
		if key not in biprob:
			biprob[key] = {}
			count[key] = 0
		if data[i] not in biprob[key]:
			biprob[key][data[i]] = 0
		biprob[key][data[i]] += 1
		count[key] += 1
	for i in biprob:
		for j in biprob[i]:
			biprob[i][j] = biprob[i][j] / count[i]
	with open(outfile, 'wb') as f:
		pickle.dump(biprob, f)
	# print biprob

def unigram(infile, outfile):
	fp = open(infile, "r")
	data = fp.read().split()
	fp.close()
	uniprob = {}
	for i in range(len(data)):
		key = data[i]
		if key not in uniprob:
			uniprob[key] = 0
		uniprob[key] += 1
	for i in uniprob:
		uniprob[i] = (uniprob[i] * 1.0)/len(data)
	with open(outfile, 'wb') as f:
		pickle.dump(uniprob, f)
	# print uniprob