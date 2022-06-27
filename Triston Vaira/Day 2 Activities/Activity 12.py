def user_io():
    content = []
    while True:
        words = input("Please enter a word: ")
        if not words:
            break
        else:
            content.append(words)
    return(content)
