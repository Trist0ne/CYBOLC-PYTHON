def leetString(s):
    cap = []
    for index, c in enumerate(s):
        if index % 2 == 0:
            cap.append(c.upper())
        else:
            cap.append(c.lower())
    return ''.join(cap)
            
print(leetString("HELLO"))
        