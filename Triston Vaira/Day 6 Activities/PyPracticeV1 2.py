def q1(*args):
    total = 0
    count = 0 
    for num in args:
        total += num
    for x in args:
        count += 1
        
    return(total/count)