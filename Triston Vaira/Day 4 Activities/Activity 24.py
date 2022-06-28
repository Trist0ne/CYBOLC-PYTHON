def diffwords(fname, words):
    set1 = set(words)
    file = open(fname)
    list1 = list(file.read().split())
    set2 = set(list1)
    return(set2.difference(set1))