Use python to produce code below that will perform the following:

Create a function called infinitearguments that will:
Print to standard output all positional arguments, in the order received, on separate lines.
Followed immediately by all keyword arguments in the form keyword=value in keyword alphabetic order.

def infinitearguments(*args,**kwargs):
    for arg in args:
        print(arg)
    keywords = dict(sorted(kwargs.items()))
    for x,y in keywords.items():
        print(f"{x}={y}")
    
        