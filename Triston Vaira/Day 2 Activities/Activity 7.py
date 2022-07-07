# Use python to produce code below that will perform the following:

# Read input from the user, the input will be an integer.
# Determine which of the following categories the number fits into an print this to the user:
# Negative Even
# Negative Odd
# Zero
# Positive Even
# Positive Odd

##############################################################################
##############################################################################

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

