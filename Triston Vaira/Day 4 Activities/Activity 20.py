import hashlib
def get_hash(data="python"):
    str = data
    encoded_str = str.encode()
    obj_sha3_256 = hashlib.sha3_256(encoded_str)
    str = obj_sha3_256
    return(str.hexdigest())

