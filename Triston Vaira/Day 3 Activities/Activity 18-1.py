def tough_read(fname):
    '''
    Sometimes my cousin is just mean. He sent me a file with a special message 
    but made it into a crazy series of ones and zeros. He told me each letter 
    was on its own line and could be converted into an ASCII character, 
    whatever that means. Can you help me by decoding his message?
    Args:
        fname (str): path to a file where the input is located
    Returns:
        str: Sentence that was decoded
    '''
    pass 

def tough_read(fname):
    infile = open(fname)
    for line in infile:
        return "B" + ''.join([chr(int(x, 2)) for x in infile])