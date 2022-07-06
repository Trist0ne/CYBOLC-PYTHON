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