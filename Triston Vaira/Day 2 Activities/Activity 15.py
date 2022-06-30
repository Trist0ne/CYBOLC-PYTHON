def disect(lst):
    '''
    Returns a tuple of the given list split into two equally sized halves.
    The given list will always consist of an even number of elements.
    Args:
        lst (lst): a list of elements
    Returns:
        tuple: a tuple of two lists
    '''
    pass    

def disect(lst):
    length = len(lst)
    middle_index = length//2
    first_half = lst[:middle_index]
    second_half = lst[middle_index:]
    stuple = (first_half, second_half)
    return(stuple)

    

    