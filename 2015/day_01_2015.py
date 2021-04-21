# Day 1: Not Quite Lisp
# <ryc> 2021

def inputdata():
    with open('day_01_2015.input') as stream:
        data = stream.readline()
    return data

def get_count(data):
    count = 0
    for char in data:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
    return count

def get_position(data):
    count = 0
    for index, char in enumerate(data):
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count == -1:
            return index + 1

def run():
    print( '\nDay 1: Not Quite Lisp' )
    data = inputdata( )
    print('\ncount =', get_count(data))
    print('\nposition =', get_position(data))

if __name__ == '__main__':
    run()
