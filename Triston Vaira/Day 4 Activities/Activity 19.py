def grab(lst):
    '''
    Returns a randomly chosen item from the given list (lst).
    Args:
        lst (list): a list of items
    Returns:
        item (?): an item from the list
    '''    

import random
def grab(lst):
    item = random.choice(lst)
    return(item)
