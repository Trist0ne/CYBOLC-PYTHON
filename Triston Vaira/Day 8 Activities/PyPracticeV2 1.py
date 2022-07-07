# Given a string of multiple words separated by single spaces, return a new string 
# with the sentence reversed. The words themselves should remain as they are.

# For example, given 'it is accepted as a masterpiece on strategy', the returned string 
# should be 'strategy on masterpiece a as accepted is it'.

# def q1(sentence):
#     pass

##############################################################################
##############################################################################

def q1(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence
        