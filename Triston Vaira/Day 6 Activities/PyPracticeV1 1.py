Given the floatstr, which is a comma separated string of floats, return a list with each of the floats in the argument as elements in the list.

def q1(floatstr):  
    pass

def q1(floatstr):
    split = floatstr.split(',')
    numbs = [float(i) for i in split]
    return(numbs)