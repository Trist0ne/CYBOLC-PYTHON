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