def infinitearguments(*args,**kwargs):
    for arg in args:
        print(arg)
    keywords = dict(sorted(kwargs.items()))
    for x,y in keywords.items():
        print(f"{x}={y}")
    
        