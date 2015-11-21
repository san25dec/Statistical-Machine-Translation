import ngram as ng

ng.trigram("../CleanedEnglish10000.txt", "../trigramEnglish10000.dict")
ng.bigram("../CleanedEnglish10000.txt", "../bigramEnglish10000.dict")
ng.unigram("../CleanedEnglish10000.txt", "../unigramEnglish10000.dict")

