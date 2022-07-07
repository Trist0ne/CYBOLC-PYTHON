# Given a linux file mode (permissions) as an integer, return the permission string that the mode represents.

# Example 1:
# mode = 511 
# 511 == 0b111111111
# permissons = 'rwxrwxrwx'

# Example 2:
# mode = 424
# 424 == 0b110101000
# permissions = 'rw-r-x---'
# def perms(mode):
#     pass

##############################################################################
##############################################################################

def perms(mode):
    pass
    strng = ""
    if mode&0x100:
        strng += "r"
    else:
        strng += "-"
    if mode&0x080:
        strng += "w"
    else:
        strng += "-"
    if mode&0x040:
        strng += "x"
    else:
        strng += "-"
    if mode&0x020:
        strng += "r"
    else:
        strng += "-"
    if mode&0x010:
        strng += "w"
    else:
        strng += "-"
    if mode&0x008:
        strng += "x"
    else:
        strng += "-"
    if mode&0x004:
        strng += "r"
    else:
        strng += "-"
    if mode&0x002:
        strng += "w"
    else:
        strng += "-"
    if mode&0x001:
        strng += "x"
    else:
        strng += "-"
    return strng
    mode = int(input("mode = ",))
    print(f"{mode} == {bin(mode)}")
    print("permissions == ", perms(mode))