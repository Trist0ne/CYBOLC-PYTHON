def infinitearguments(*args,**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))