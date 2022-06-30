Use python to produce code below that will perform the following:

Create a variable named sentence and assign the value 'good for all'
Turn the sentence variable into a list of individual characters and assign this to a variable named sent_list.
Change the first (index 0) character in the list to 'f'
Change the last (index -1) character in the list to '?'
Combine the list into a new string with periods ('.') in between each character and assign the result to a new variable named output.
NOTE: Do not indent your code

import string
from turtle import st
from psutil import sensors_temperatures


sentence = 'good for all'
sent_list = list(sentence)
sent_list[0] = 'f'
sent_list[-1] = '?'
output = '.'.join(sent_list)