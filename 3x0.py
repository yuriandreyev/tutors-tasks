'''this module finds all 3-digit numbers which start at 3 and ends by 0 in file.'''

import re


def find_3digit_numbers(file_name):
    ''' Function finds and returns three-digit numbers which start at 3 and ends by 0 '''
    with open(file_name) as my_file:
        text = my_file.read()
    template = re.compile(' 3\d0 ')
    res = template.findall(text)
    return res

print(find_3digit_numbers('text3x0.txt'))
