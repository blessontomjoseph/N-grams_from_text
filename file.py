def ngrams(n, path):
    """produces a dictionary with unique ngrams as keys and its frequency as values from a corpus.

    Args:
        n (int): ngram size
        path (str): path to text file of corpus

    Returns:
        dict: unique ngram pairs as key, and its frequency as values.
    """
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