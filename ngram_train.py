import ngram as ng

ng.trigram("../CleanedEnglish100.txt", "../trigramEnglish100.dict")
ng.bigram("../CleanedEnglish100.txt", "../bigramEnglish100.dict")
ng.unigram("../CleanedEnglish100.txt", "../unigramEnglish100.dict")

