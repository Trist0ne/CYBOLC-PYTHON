def make_tuple(a,b):
    c = (b+1)
    range1 = range(a,c)
    stuple = ()
    for i in range1:
        if i%10 == 0:
            fuple = (i,)
            stuple += fuple 
    return(stuple)
