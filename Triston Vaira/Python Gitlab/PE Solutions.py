#Practice Exam Solutions


#1
# #  TLO: 112-SCRPY002, LSA 3,4
# #  Given the floatstr, which is a comma separated string of
# #  floats, return a list with each of the floats in the 
# #  argument as elements in the list.

def q1(floatstr):
    new_values = []
    for digit in floatstr.split(', '):
        new_values.append(float(digit))
    return new_values

###########################################################################################################################################

#2
#  TLO: 112-SCRPY006, LSA 3
#  TLO: 112-SCRPY007, LSA 4
#  Given the variable length argument list, return the average
#  of all the arguments as a float
 
def q2(*args):
    sum = 0
    counter = 0
    for value in args:
        sum += value
        counter += 1
        average = sum / counter
    return average

###########################################################################################################################################

#3
#  TLO: 112-SCRPY004, LSA 3
#  Given a list (lst) and a number of items (n), return a new 
#  list containing the last n entries in lst.

def q3(lst,n):
    return lst[len(lst)-n:]

########################################################################################################################################### 

#4
#  TLO: 112-SCRPY004, LSA 1,2
#  TLO: 112-SCRPY006, LSA 3
#  Given an input string, return a list containing the ordinal numbers of 
#  each character in the string in the order found in the input string.

def q4(strng):
    new_values = []
    for chr in strng:
        new_values.append(ord(chr))
    return new_values

###########################################################################################################################################

#5
#  TLO: 112-SCRPY002, LSA 1,3
#  TLO: 112-SCRPY004, LSA 2
#  Given an input string, return a tuple with each element in the tuple
#  containing a single word from the input string in order.
 
def q5(strng):
 strng = strng.split()
 return sorted(strng, key = str.casefold)


###########################################################################################################################################

#6
#  TLO: 112-SCRPY007, LSA 2
#  Given a dictionary (catalog) whose keys are product names and values are product
#  prices per unit and a list of tuples (order) of product names and quantities,
#  compute and return the total value of the order.
 
#  Example catalog:
#  {
#  'AMD Ryzen 5 5600X': 289.99,
#  'Intel Core i9-9900K': 363.50,
#  'AMD Ryzen 9 5900X': 569.99
#  }
 
#  Example order:
#  [
#  ('AMD Ryzen 5 5600X', 5), 
#  ('Intel Core i9-9900K', 3)
#  ]
 
#  Example result:
#  2540.45 
 
#  How the above result was computed:
#  (289.99 * 5) + (363.50 * 3)
 
def q6(catalog, order):
    runner = 0
    for item in catalog:
        for invoice in order:
            if item == invoice[0]:
                runner += (catalog[item] * invoice[1])
    return runner

###########################################################################################################################################

#7
#  TLO: 112-SCRPY005, LSA 1
#  Given a filename, open the file and return the length of the first line 
#  in the file excluding the line terminator.
 
def q7(filename):
    with open(filename) as fp:
        return len(fp.readline().strip())

###########################################################################################################################################

#8
#  TLO: 112-SCRPY003, LSA 1
#  TLO: 112-SCRPY004, LSA 1,2
#  TLO: 112-SCRPY005, LSA 1
#  Given a filename and a list, write each entry from the list to the file
#  on separate lines until a case-insensitive entry of "stop" is found in 
#  the list. If "stop" is not found in the list, write the entire list to 
#  the file on separate lines.

def q8(filename,lst):
    with open(filename, 'w') as fp:
        for i in lst:
            if str.casefold(i) != 'stop':
                fp.write(i + '\n')

###########################################################################################################################################

#9
# TLO: 112-SCRPY003, LSA 1
#  Given the military time in the argument miltime, return a string 
#  containing the greeting of the day.
#  0300-1159 "Good Morning"
#  1200-1559 "Good Afternoon"
#  1600-2059 "Good Evening"
#  2100-0259 "Good Night"
 
def q9(miltime):
    if (miltime >= 300) and (miltime <= 1159):
        return "Good Morning"
    elif (miltime >= 1200) and (miltime <= 1559):
        return "Good Afternoon"
    elif (miltime >= 1600) and (miltime <= 2059):
        return "Good Evening"
    else:
        return "Good Night"

###########################################################################################################################################

#10
#  TLO: 112-SCRPY003, LSA 1
#  TLO: 112-SCRPY004, LSA 1
#  Given the argument numlist as a list of numbers, return True if all 
#  numbers in the list are NOT negative. If any numbers in the list are
#  negative, return False.

def q10(numlist):
    for num in numlist:
        if num != abs(num):
            return False
        else:
            return True