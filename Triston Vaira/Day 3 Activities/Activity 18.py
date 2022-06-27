def linenums(inpath, outpath):
    infile = open(inpath)
    output = open(outpath, "w")
    n = 1
    for line in infile:
        newline = (str(n) + ": " + line)
        output.write(newline)
        n += 1
     
        