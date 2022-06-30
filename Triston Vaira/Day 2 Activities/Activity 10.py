Use python to produce code below that will perform the following:

Given a mixed case string as parameter s
Capitalize every letter with an even index within the string.
Lowercase every letter with an odd index within the string.
Return the resulting string.
Example - Given: "ABCDEF ghijkl" Return: "AbCdEf gHiJkL"
def leetString(s):
    pass 

def leetString(s):
    cap = []
    for index, c in enumerate(s):
        if index % 2 == 0:
            cap.append(c.upper())
        else:
            cap.append(c.lower())
    return ''.join(cap)
            
print(leetString("HELLO"))
        