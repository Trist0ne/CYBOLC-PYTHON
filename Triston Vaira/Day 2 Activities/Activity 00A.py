fizz = int(input("Please enter a number: "))

if (fizz%3 != 0) and (fizz%5 != 0):
    print(fizz)
elif (fizz%3 == 0) and (fizz%5 == 0):
    print("fizzbuzz")
elif (fizz%3 == 0):
    print("fizz")
elif (fizz%5 == 0):
    print("buzz")
