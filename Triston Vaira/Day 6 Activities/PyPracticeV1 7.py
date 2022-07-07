# Given a filename, open the file and return the length of the first line in the file excluding the line terminator.

# def q1(filename):
#     pass

##############################################################################
##############################################################################

def q1(filename):
    with open(filename, 'r') as file:
        for line in file:
            return(len(line)-1)