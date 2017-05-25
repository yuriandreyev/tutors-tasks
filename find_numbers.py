'''this module finds all numbers in text.'''

import re


def find_numbers(file_name):
    ''' Function finds and returns numbers in text from file '''
    with open(file_name) as my_file:
        text = my_file.read()
    template = re.compile('\d+')
    res = template.findall(text)
    return res

print(find_numbers('text_numbers.txt'))


