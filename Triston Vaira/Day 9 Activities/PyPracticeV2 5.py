# Given an integer and limit, return a list of even multiples of the integer up to and including the limit.

# For example, if integer = 3 and limit = 30, the returned list should be [0,6,12,18,24,30]. Note, 0 is a multiple of any integer except 0 itself.

# def q1(integer, limit):
#     pass

##############################################################################
##############################################################################

def q1(integer, limit):
    lst = []
    for i in range(0, limit + 1, integer):
        if i % 2 == 0:
            lst.append(i)
    return(lst)