def round_to_position(lst):
    rounded = []
    n = 0
    for int in lst:
        rounded_number = round(int, n)
        rounded.append(rounded_number)
        n = n+1
    return(rounded)