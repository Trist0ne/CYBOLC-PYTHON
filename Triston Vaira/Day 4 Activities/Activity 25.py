from collections import Counter

def count_words(filepath):
    file = open(filepath)
    list1 = list(file.read().split())
    word_counts = Counter(list1)
    return(word_counts)