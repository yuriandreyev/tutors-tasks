''' This module reads the number from file and writes Pifagor's table
of number to the same file. Script gets file's name from command line '''

import sys

def read_number(file_name):
    ''' Function takes file's name as argument, reads number from the file
    and returns it as integer '''
    with open(file_name) as myfile:
        number = myfile.readline()
        number.rstrip()
    return int(number)

def calc_table(number):
    ''' Function takes a number as argument and calculates Pifagor's table of the number '''
    raw = col = list(range(1,number+1))
    result_table = []
    
    for num in raw:
        result_raw = []
        for numb in col:
            result_raw.append(str(num*numb))
        result_table.append(result_raw)
    return result_table

def output_result(file_name):
    ''' Function takes file's name as arg, read a number from the file and
    writes to the file Pifagor's table of the number '''
    number = read_number(file_name)
    result = calc_table(number)
    with open('numbers.txt', 'w') as myfile:
        myfile.write(str(number)+ '\n'*3)
        for raw in result:
            template = '{0}\n'.format('\t'.join(raw))
            myfile.write(template)

output_result(sys.argv[1])


