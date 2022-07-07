# Write a function, round_to_position, which takes a list of floats and returns a new list 
# with the original floats each rounded to the number of digits of precision after the decimal 
# point corresponding to the original float's position in the list.


##############################################################################
##############################################################################

def round_to_position(lst):
    pass

def round_to_position(lst):
    rounded = []
    n = 0
    for int in lst:
        rounded_number = round(int, n)
        rounded.append(rounded_number)
        n = n+1
    return(rounded)