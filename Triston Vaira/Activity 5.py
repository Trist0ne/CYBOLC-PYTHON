import string
from turtle import st
from psutil import sensors_temperatures


sentence = 'good for all'
sent_list = list(sentence)
sent_list[0] = 'f'
sent_list[-1] = '?'
output = '.'.join(sent_list)