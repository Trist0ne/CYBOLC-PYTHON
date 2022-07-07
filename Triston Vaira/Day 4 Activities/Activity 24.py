# Use python to produce code below that will perform the following:

# A list of words is provided in the file specified by fname.
# Another list of words is provided as the parameter words.
# Return a list of all the words found in the file that are NOT contained in the list of words in parameter.
# Each word in the file will be separated by at least one character of whitespace.
# def diffwords(fname, words):
#     pass 

##############################################################################
##############################################################################

def diffwords(fname, words):
    set1 = set(words)
    file = open(fname)
    list1 = list(file.read().split())
    set2 = set(list1)
    return(set2.difference(set1))