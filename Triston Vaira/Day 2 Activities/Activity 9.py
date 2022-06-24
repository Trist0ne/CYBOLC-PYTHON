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
