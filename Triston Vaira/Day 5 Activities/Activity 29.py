# def sort_embedded(filepath):
#     '''
#     Read all lines from file in `filepath` and return a list of all lines sorted numerically by
#     the number at character positions 10 to 15 in each line..
#     Remove all linebreaks before sorting.
    
#     Example: The embedded number is 561234 below.
#     Here is a561234 long line of text from the file.
       
#     Args:
#         filepath (str): The path to the file
#     Returns:
#         list : lines from input file numerically sorted on the embedded number without linebreaks
#     '''

##############################################################################
##############################################################################

def sort_embedded(filepath):
    with open(filepath) as file:
        lines = file.read().splitlines()
        sortedlines = sorted(lines, key=lambda len: len[9:16])
    return(sortedlines)