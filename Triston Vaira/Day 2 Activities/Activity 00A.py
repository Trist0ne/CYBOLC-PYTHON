FizzBuzz is an interview question that is said to filter out 99.5% of programming job candidates.

Add code so that it takes a number from the user and prints it (the number) if it isn’t divisible by 3 or 5. For multiples of 3 print 'fizz' instead. For multiples of 5 print 'buzz' instead. For multiples of 3 and 5 print 'fizzbuzz'.

fizz = int(input("Please enter a number: "))

if (fizz%3 != 0) and (fizz%5 != 0):
    print(fizz)
elif (fizz%3 == 0) and (fizz%5 == 0):
    print("fizzbuzz")
elif (fizz%3 == 0):
    print("fizz")
elif (fizz%5 == 0):
    print("buzz")
