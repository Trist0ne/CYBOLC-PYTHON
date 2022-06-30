def replace_in_file(in_path, out_path, reps):
    '''
    Replace all found instances of the individual tuple entries in the file
    found at in_path. Replacements will be in the list reps as a list of
    tuples. Each tuple entry will contain the 'find' as the first element and
    the 'replace' will be the second element. Write the result to the file
    specified with out_path.
    Args:
        in_path (str): input file path
        out_path (str): output file path
        reps (list): list of tuples containing ('find', 'replace') mappings
    Returns:
        None
    '''
    pass 

def replace_in_file(in_path, out_path, reps):
    with open(in_path) as src:
        content = src.read()
        
    for rep in reps:
        content = content.replace(rep[0],rep[1])
        
    with open(out_path) as dst:
        dst.write(content)