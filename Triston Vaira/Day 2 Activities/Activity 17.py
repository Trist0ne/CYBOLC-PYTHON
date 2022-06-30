def code_points(strng):
    '''
    Returns a list of ordinals for every character in the given string
    Args:
        strng (str): a string of alphanumeric characters
    Returns:
        list: ordinals of every character in the given string
    '''    
    pass

def code_points(strng):
    ords = []
    for char in strng:
        ords.append(ord(char))
    return(ords)