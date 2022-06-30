Use python to produce code below that will perform the following:

Read multiple lines from the user on standard input until an empty string is read.
Return a list of all these lines without line terminators
Each line should be reversed from how it is read in.
def reverseit():
    pass 

def reverseit():
    content = []
    while True:
        words = input("Please enter a line: ")
        words = words[::-1]
        if not words:
            break
        else:
            content.append(words)
    return(content)
    
    
reverseit()
