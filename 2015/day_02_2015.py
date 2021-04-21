# Day 2: I Was Told There Would Be No Math
# <ryc> 2021

import re

def inputdata():
    with open('day_02_2015.input') as stream:
        data = stream.readlines()
        data = [ [ int(number) for number in re.findall('\d+', line) ] for line in data ]
    return data

def get_wrapping_paper(data):
    count = 0
    for dims in data:
        surfaces = [dims[0]*dims[1], dims[1]*dims[2], dims[0]*dims[2]]
        surfaces.sort()
        count += surfaces[0] * 3 + surfaces[1] * 2 + surfaces[2] * 2
    return count

def get_ribbon(data):
    count = 0
    for dims in data:
        dims.sort()
        count += dims[0] * 2 + dims[1] * 2 + dims[0] * dims[1] * dims[2]
    return count

def run():
    print( '\nDay 2: I Was Told There Would Be No Math' )
    data = inputdata( )
    print('\nwrapping paper =', get_wrapping_paper(data))
    print('\nribbon =', get_ribbon(data))

if __name__ == '__main__':
    run()
