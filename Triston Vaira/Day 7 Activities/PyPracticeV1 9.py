# Given the military time in the argument miltime, return a string containing the greeting of the day.

# 0300-1159 "Good Morning"
# 1200-1559 "Good Afternoon"
# 1600-2059 "Good Evening"
# 2100-0259 "Good Night"
# def q1(miltime):
#     pass

##############################################################################
##############################################################################


def q1(miltime):
    if miltime >= 301 and miltime < 1200:
        print("Good Morning")
    elif miltime >= 1200 and miltime < 1600:
        print("Good Afternoon")
    elif miltime >= 1600 and miltime < 2100:
        print("Good Evening")
    elif miltime >= 2100 or miltime < 300:
        print("Good Night")


        