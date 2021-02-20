# Day 4: Passport Processing
# <ryc> 2021

import re

def inputdata( ):
    stream = open( 'day_04_2020.input' )
    data = [ ]
    record = ''
    for line in stream:
        if len( line ) == 1:
            data.append( record )
            record = ''
        else:
            record += line[ : -1 ] + ' '
    data.append( record )
    stream.close( )
    return data

def processing( data, keys ):
    valid = 0
    for record in data:
        match = 0
        for key in keys:
            if re.search( key, record ) != None:
                match += 1
        if match == len( keys ):
            valid += 1
    return valid

if __name__ == '__main__':
    print( '\nDay 4: Passport Processing' )
    data = inputdata( )
    keys = (
        'byr:',
        'iyr:',
        'eyr:',
        'hgt:',
        'hcl:',
        'ecl:',
        'pid:')
    print( "\nValidation simple =", processing( data, keys) )
    keys = (
        'byr:(19[2-9][0-9]|200[0-2]) ',
        'iyr:20(1[0-9]|20) ',
        'eyr:20(2[0-9]|30) ',
        'hgt:(1([5-8][0-9]|9[0-3])cm|([56][0-9]|7[0-6])in) ',
        'hcl:#[0-9a-f]{6} ',
        'ecl:(amb|blu|brn|gry|grn|hzl|oth) ',
        'pid:[0-9]{9} ')
    print( "\nValidation final =", processing( data, keys) )
