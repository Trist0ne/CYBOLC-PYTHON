def get_type_str(obj):
    if type(obj) is str:
        return("string")
    elif type(obj) is int:
        return("integer")
    elif type(obj) is bool:
        return("boolean")
    elif type(obj) is float:
        return("float")
    elif type(obj) is list:
        return("list")
    elif type(obj) is tuple:
        return("tuple")
    else:
        return("unknown")
    
