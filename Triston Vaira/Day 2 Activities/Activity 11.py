def evensandodds(first, last):
    for num in range(first, last + 1):
        if num % 2 == 0:
            print(num)
    for num in range(first, last + 1):
        if num % 2 != 0:
            print(num)
            
            