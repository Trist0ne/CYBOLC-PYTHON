Use python to produce code below that will create several named variables with the specified value using the str.format member function. You may assign any value for the variables other than output. The output variable must use the same boilerplate text and include the appropriate values assigned to the first three.

Identifier	Example Value	Type
name	Jerry	str
greeting	Sir	str
time	noon	str
output	Hello Jerry! Sir, will you be arriving by noon?	str
NOTE: Do not indent your code

name = 'Jerry'
greeting = 'Sir'
time = 'noon'
output = 'Hello {}! {}, will you be arriving by {}?'.format(name,greeting,time)
