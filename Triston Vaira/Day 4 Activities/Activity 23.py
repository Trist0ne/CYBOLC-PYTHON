# def get_type_str(obj):
#     '''
#     Returns the type of the parameter as a string.
#     Possible types are:
    

      
# string

      
# boolean

      
# integer

      
# float

      
# list

      
# tuple

    

#     NOTE: Any other types should be identified with 'unknown'
       
#     Args:
#         obj (?): The object that should be classified
#     Returns:
#         str : The type of the provided data


##############################################################################
##############################################################################

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
    
