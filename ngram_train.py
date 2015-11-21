import ngram as ng

ng.trigram("../CleanedEnglish1000.txt", "../trigramEnglish1000.dict")
ng.bigram("../CleanedEnglish1000.txt", "../bigramEnglish1000.dict")
ng.unigram("../CleanedEnglish1000.txt", "../unigramEnglish1000.dict")

