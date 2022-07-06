def q1(miltime):
    if miltime >= 301 and miltime < 1200:
        print("Good Morning")
    elif miltime >= 1200 and miltime < 1600:
        print("Good Afternoon")
    elif miltime >= 1600 and miltime < 2100:
        print("Good Evening")
    elif miltime >= 2100 or miltime < 300:
        print("Good Night")


        