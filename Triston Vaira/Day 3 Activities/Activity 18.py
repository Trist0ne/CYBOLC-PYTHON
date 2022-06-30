Use python to produce code below that will perform the following:

Read file specified by the path in inpath parameter and write all lines to the file specified by the outpath parameter.
Before writing out each line, add the line number starting with 1 follow by colon and space.
def linenums(inpath, outpath):
    pass 


def linenums(inpath, outpath):
    infile = open(inpath)
    output = open(outpath, "w")
    n = 1
    for line in infile:
        newline = (str(n) + ": " + line)
        output.write(newline)
        n += 1
     
        