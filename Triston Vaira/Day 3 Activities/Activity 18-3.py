def replace_in_file(in_path, out_path, reps):
    with open(in_path) as src:
        content = src.read()
        
    for rep in reps:
        content = content.replace(rep[0],rep[1])
        
    with open(out_path) as dst:
        dst.write(content)