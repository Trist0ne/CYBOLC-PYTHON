# def user_io():
#     '''
#     Returns a list of items read from the user until the user enters an empty string.

#     Args:
#         None
#     Returns:
#         list: a list of strings
#     '''    
#     pass

##############################################################################
##############################################################################


def user_io():
    content = []
    while True:
        words = input("Please enter a word: ")
        if not words:
            break
        else:
            content.append(words)
    return(content)
