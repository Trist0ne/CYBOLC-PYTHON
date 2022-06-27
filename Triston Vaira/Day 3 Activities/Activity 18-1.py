def tough_read(fname):
    infile = open(fname)
    for line in infile:
        return "B" + ''.join([chr(int(x, 2)) for x in infile])