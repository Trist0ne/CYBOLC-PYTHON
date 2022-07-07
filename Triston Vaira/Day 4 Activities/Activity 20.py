# def get_hash(data="python"):
#     '''
#     Returns the SHA3 256-bit hash of the data provided.
#     You will need to use the hashlib python library to complete this challenge.
       
#     NOTE: The first call will use the string "python" later calls will use random strings
#     NOTE: You can convert a string into a bytes-like object which is needed for hashing with: 
             
#     data.encode("utf-8")
    
#     NOTE: You can create a bytes-like object out of a literal by adding a b in front of the string, ie b"python" or b'python'
       
#     Args:
#         data (str): data to be encoded
#     Returns:
#         str : The SHA3 256-bit hash of the provided data
#     '''    

##############################################################################
##############################################################################

import hashlib
def get_hash(data="python"):
    str = data
    encoded_str = str.encode()
    obj_sha3_256 = hashlib.sha3_256(encoded_str)
    str = obj_sha3_256
    return(str.hexdigest())

