# def numsys(startint):
#     """ Given an integer `startint`, convert this integer to its 
#     binary version, octal version, and hexadecimal version and 
#     return these as a tuple in the order given. """
#     pass
    
# def getints(binnum, octnum, decnum, hexnum):
#     """ Given the string parameters `binnum` (binary number), 
#     `octnum` (octal number), decnum` (decimal number), `hexnum` 
#     (hexadecimal number), convert each of these  to an integer and 
#     return them as a list in their parameter order. """
#     pass
    
# def literals():
#     """ Create a list and set the value using literals and return 
#     the list. All literals will represent the decimal integer value 
#     1,000,000 (one million). You must use a literal to represent 
#     the target value in binary, hexadecimal, decimal, and octal.
#     The order is not important. """
#     pass

##############################################################################
##############################################################################


def numsys(startint):
    hold = startint
    a = bin(hold)
    b = oct(hold)
    c = hex(hold)
    num1 = (a, b, c)
   
    return num1
   
def getints(binnum, octnum, decnum, hexnum):
    d = int(binnum, 2)
    e = int(octnum, 8)
    f = int(decnum)
    g = int(hexnum, 16)
    num2 = [d, e, f, g]
   
    return num2
   
def literals():
    num = [0b11110100001001000000, 0o3641100, 0xf4240, 1000000]   
    return num