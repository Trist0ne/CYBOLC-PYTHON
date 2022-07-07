
# Given a password as a string, return an integer whose bits are set according to the following rules:

# 0x1 - Consists of at least 15 characters
# 0x2 - Consists of at least 1 number
# 0x4 - Consists of at least 1 uppercase letter
# 0x8 - Consists of at least 1 lowercase letter
# 0x10 - Consists of at least 1 special character (~!"@#$%^&'*_-+=`|(){}[]:;<>,.?/)
# Note: The set of special characters corresponds exactly with those characters in string.punctuation

# def complexity(password):
#     pass

##############################################################################
##############################################################################

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