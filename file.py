def ngrams(n, path):
    file = open(path, 'r')
    text = file.read()
    sentences = text.split('\n')
    n_grams = {}
    for sentence in sentences:
        words = sentence.split(" ")
        for value in range(len(words)-n+1):
            unique_n_gram = tuple(words[value:value+n])
            if unique_n_gram not in n_grams.keys():
                n_grams[unique_n_gram] = 1
            else:
                n_grams[unique_n_gram] += 1
    return n_grams
