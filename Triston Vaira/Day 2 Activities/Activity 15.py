def disect(lst):
    length = len(lst)
    middle_index = length//2
    first_half = lst[:middle_index]
    second_half = lst[middle_index:]
    stuple = (first_half, second_half)
    return(stuple)

    

    