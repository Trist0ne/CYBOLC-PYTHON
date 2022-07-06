import string
import re

def complexity(password):
    x = 0
    pw = password
    
    if len(pw) >= 15:
        x |= 0x1
    if re.match('.*[0-9]', pw):
        x |= 0x2
    if re.match('.*[A-Z]', pw):
        x |= 0x4
    if re.match('.*[a-z]', pw):
        x |= 0x8

 

    for n in pw:
        if n in string.punctuation:
            x |= 0x10

 

    return x