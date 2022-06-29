def sort_ascii(filepath):
    with open(filepath) as file:
        lines = file.read().splitlines()
        lines.sort(key=str.lower)
    return(lines)
    
