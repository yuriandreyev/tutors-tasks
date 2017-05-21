'''This module reads the number from file and writes Pifagor's table
of number to the same file. Script gets file's name from command line'''

import sys

def read_number(file_name):
    with open(file_name) as myfile:
        number = myfile.readline()
        number.rstrip()
    return int(number)

def calc_table(number):
    raw = col = list(range(1,number+1))
    result_table = []
    
    for num in raw:
        result_raw = []
        for numb in col:
            result_raw.append(str(num*numb))
        result_table.append(result_raw)
    return result_table

def output_result(file_name):
    number = read_number(file_name)
    result = calc_table(number)
    with open('numbers.txt', 'w') as myfile:
        myfile.write(str(number)+ '\n'*3)
        for raw in result:
            template = '{0}\n'.format('\t'.join(raw))
            myfile.write(template)

output_result(sys.argv[1])


