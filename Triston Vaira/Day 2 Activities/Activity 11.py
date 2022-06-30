Use python to produce code below that will perform the following:

Print out every even number on a separate line from parameters first to last, inclusive.
Next print out every odd number from first to last, inclusive.
def evensandodds(first, last):
    pass 

def evensandodds(first, last):
    for num in range(first, last + 1):
        if num % 2 == 0:
            print(num)
    for num in range(first, last + 1):
        if num % 2 != 0:
            print(num)
            
            