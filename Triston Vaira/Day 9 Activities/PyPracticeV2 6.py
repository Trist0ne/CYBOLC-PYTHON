# Given two filenames, return a list whose elements consist of line numbers for which the two files differ. 
# The first line is considered line 0.

# def q1(f0, f1):
#     pass


##############################################################################
##############################################################################

def q1(f0, f1):
    f0 = (open(f0).read()).split("\n")
    f1 = (open(f1).read()).split("\n")
    lst = []
    for i in range(len(f0)):
        if f0[i] != f1[i]:
            lst.append(i)
    return(lst)
