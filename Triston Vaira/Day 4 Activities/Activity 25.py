def count_words(filepath):
    '''
    Count the occurrences of each word in the file. Create a dictionary that contains each word in the file as a key
    and the value for each key will contain the number of times each words is found in the file. Words will be
    separated by one or more whitespace characters spread over multiple lines.
       
    Args:
        filepath (str): The path to the file
    Returns:
        dict : keys - words
               values - number of times each word appears
    '''

from collections import Counter

def count_words(filepath):
    file = open(filepath)
    list1 = list(file.read().split())
    word_counts = Counter(list1)
    return(word_counts)