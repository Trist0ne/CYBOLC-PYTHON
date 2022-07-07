# Write a script that implements a function, find_product, which takes two numbers and returns 
# the product. Use the name=='__main__' idiom to prompt the user for two integers a print the result of calling 
# find_product using those integers.

##############################################################################
##############################################################################

def find_product(num1,num2):
    return(num1*num2)
    

if __name__=='__main__':
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    print(find_product(num1,num2))
