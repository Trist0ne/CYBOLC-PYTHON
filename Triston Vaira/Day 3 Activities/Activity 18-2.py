def log_to_file(fname, theme):
    outfile = open(fname, "a")
    while True:
        inspi = input("Please enter your inspiration: ")
        if inspi == "":
            break
        else:
            outfile.write(theme + ":" + inspi + "\n")
