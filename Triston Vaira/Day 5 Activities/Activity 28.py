def sort_length(filepath):
    with open(filepath) as file:
        lines = file.read().splitlines()
        sortedlines = sorted(lines, key=len)
        arranged = sortedlines[::-1]
    return(arranged)
