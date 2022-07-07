# Given two lists of integers, return a sorted list that contains all integers from both lists in descending order.

# For example, given [3,4,9] and [8,1,5] the returned list should be [9,8,5,4,3,1]. The returned list may contain duplicates.

# def q1(lst0, lst1):
#     pass

##############################################################################
##############################################################################


def q1(lst0, lst1):
    res = sorted(lst0 + lst1, reverse=True)
    return(res)
        