# Given the argument numlist as a list of numbers, return True if all numbers in the list are NOT negative. 
# If any numbers in the list are negative, return False.

# def q1(numlist):
#     pass

##############################################################################
##############################################################################

def q1(numlist):
    for i in numlist:
        if i < 0:
            return False
    return True