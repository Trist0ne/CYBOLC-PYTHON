import statistics
def q1(s1,s2,s3):
    scores = [s1,s2,s3]
    avg = statistics.mean(scores)
    if avg > 50:
        return("GO")
    else:
        return("NOGO")
        
        