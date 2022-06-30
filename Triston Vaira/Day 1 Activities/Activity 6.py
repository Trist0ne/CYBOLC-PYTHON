Use python to produce code below that will perform the following:

Read multiple numbers separated by spaces on the same line from the user.
Change all spaces to a plus sign.
Print the resulting string to the user.
NOTE: Do not indent your code



from docutils import SettingsSpec


numbers = input('Enter your numbers, seperated by spaces: ')
string = numbers.replace(" ", "+")
print(string)