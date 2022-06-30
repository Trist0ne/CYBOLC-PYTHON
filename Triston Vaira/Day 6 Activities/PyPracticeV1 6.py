def q6(catalog, order):
    total = 0
    for x in order:
        total = x[1] * catalog.get(x[0])
    return(total)