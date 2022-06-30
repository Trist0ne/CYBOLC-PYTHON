def q1(filename):
    with open(filename, 'r') as file:
        for line in file:
            return(len(line)-1)