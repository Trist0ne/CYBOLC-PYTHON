def sort_embedded(filepath):
    with open(filepath) as file:
        lines = file.read().splitlines()
        sortedlines = sorted(lines, key=lambda len: len[9:16])
    return(sortedlines)