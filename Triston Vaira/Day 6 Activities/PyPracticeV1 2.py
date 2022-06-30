Given the variable length argument list, return the average of all the arguments as a float

def q1(*args):
    pass

def q1(*args):
    total = 0
    count = 0 
    for num in args:
        total += num
    for x in args:
        count += 1
        
    return(total/count)