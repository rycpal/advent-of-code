# Day 1: Report Repair
# <ryc> 2021

def inputdata( ):
    stream = open( 'day_01_2020.input' )
    numbers = [ ]
    for line in stream:
        numbers.append( int( line ) )
    stream.close( )
    return numbers

def sum_two( numbers ):
    for i in numbers[ : -1 ]:
        for j in numbers[ 1 : ]:
            if( i + j == 2020 ):
                return ( i, j )

def sum_three( numbers ):
    for i in numbers[ : -2 ]:
        for j in numbers[ 1 : -1 ]:
            for k in numbers[ 2 : ]:
                if( i + j + k == 2020 ):
                    return ( i, j, k )

if __name__ == '__main__':
    print( '\nDay 1: Report Repair ' )
    numbers = inputdata( )
    ( obj1, obj2 ) = sum_two( numbers )
    print( f'\n{ obj1 } + { obj2 } = { obj1 + obj2 }' )
    print( f'{ obj1 } * { obj2 } = { obj1 * obj2 }' )
    ( obj1, obj2, obj3 ) = sum_three( numbers )
    print( f'\n{ obj1 } + { obj2 } + { obj3} = { obj1 + obj2 + obj3 }' )
    print( f'{ obj1 } * { obj2 } * { obj3} = { obj1 * obj2 * obj3 }' )
