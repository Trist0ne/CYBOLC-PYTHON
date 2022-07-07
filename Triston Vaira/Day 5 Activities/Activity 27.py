# def sort_ascii(filepath):
#     '''
#     Read all lines from file in `filepath` and return a list of all lines in case-insensitive ASCII order.
#     Remove all linebreaks before sorting.
       
#     Args:
#         filepath (str): The path to the file
#     Returns:
#         list : lines from input file sorted into ASCII order without linebreaks
#     '''

##############################################################################
##############################################################################

def sort_ascii(filepath):
    with open(filepath) as file:
        lines = file.read().splitlines()
        lines.sort(key=str.lower)
    return(lines)
    
