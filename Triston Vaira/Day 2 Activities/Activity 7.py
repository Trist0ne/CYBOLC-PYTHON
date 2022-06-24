from ast import If


number = int(input("Please type a number: "))
if number == 0:
    print("Zero")
elif (number < 0) and (number%2 == 0):
    print("Negative Even")
elif (number < 0) and (number%2 != 0):
    print("Negative Odd")
elif (number > 0) and (number%2 == 0):
    print("Positive Even")
else:
    print("Positive Odd")

