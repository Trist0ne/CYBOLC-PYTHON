def log_to_file(fname, theme):
    '''
    You have a artist friend that likes to jot down some inspirational words
    when the mood strikes. These fits of inspiration always have a theme that
    he needs to remember with the messages. Your friend needs some help
    keeping track. Read each of the inspirational messages from the user and
    write them to the end of the file specified by fname. Since the theme is
    important and must be remembered, add the theme and a colon before each
    message and ensure each inspirational message is on its own line. An empty
    input will indicate no more entries and the end of the theme.
    Args:
        fname (str): Path to an existing file that includes previous
                     inspirational messages to keep.
        theme (str): Theme to be placed on each line.
    Returns:
        None
    '''
    pass 

def log_to_file(fname, theme):
    outfile = open(fname, "a")
    while True:
        inspi = input("Please enter your inspiration: ")
        if inspi == "":
            break
        else:
            outfile.write(theme + ":" + inspi + "\n")
