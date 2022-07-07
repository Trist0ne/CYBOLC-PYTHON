# Given a filename and a list, write each entry from the list to the file on separate lines 
# until a case-insensitive entry of "stop" is found in the list. If "stop" is not found 
# in the list, write the entire list to the file on separate lines.

# def q1(filename,lst):
#     pass

##############################################################################
##############################################################################

def q1(filename,lst):
    with open(filename, 'a') as file:
        while True:
            for x in lst:
                if x = "stop":
                    break
                else:
                    file.write(x)

        