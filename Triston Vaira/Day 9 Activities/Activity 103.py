# Given a filename and a list, write each entry from the list to the file on separate lines 
# until a case-insensitive entry of "stop" is found in the list. If "stop" is not found in the list, 
# write the entire list to the file on separate lines.

# def q1(filename,lst):
#     pass

#########################################################################################################

def q1(filename,lst):
    with open(filename, 'w') as file:
            for x in lst:
                if x.lower() != 'stop':
                    file.write(x + '\n')
                else:
                    break