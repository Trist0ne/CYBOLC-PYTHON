# def sort_length(filepath):
#     '''
#     Read all lines from file in `filepath` and return a list of all lines sorted longest to shortest.
#     Remove all linebreaks before sorting.
       
#     Args:
#         filepath (str): The path to the file
#     Returns:
#         list : lines from input file sorted longest to shortest without linebreaks
#     '''

##############################################################################
##############################################################################

def sort_length(filepath):
    with open(filepath) as file:
        lines = file.read().splitlines()
        sortedlines = sorted(lines, key=len)
        arranged = sortedlines[::-1]
    return(arranged)
