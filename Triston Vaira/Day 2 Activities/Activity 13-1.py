# def make_tuple(a,b):
#     '''
#     Returns a tuple of the multiples of 10 from a to b inclusive.
#     Args:
#         None
#     Returns:
#         tuple: a tuple of the multiples of 10 from a to b inclusive
#     '''    
    
##############################################################################
##############################################################################

def make_tuple(a,b):
    c = (b+1)
    range1 = range(a,c)
    stuple = ()
    for i in range1:
        if i%10 == 0:
            fuple = (i,)
            stuple += fuple 
    return(stuple)
