# Given 3 scores in the range [0-100] inclusive, return 'GO' if the average score is greater than 50. Otherwise return 'NOGO'.

# def q1(s1,s2,s3):
#     pass

##############################################################################
##############################################################################

import statistics
def q1(s1,s2,s3):
    scores = [s1,s2,s3]
    avg = statistics.mean(scores)
    if avg > 50:
        return("GO")
    else:
        return("NOGO")
        
        