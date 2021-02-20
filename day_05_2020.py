# Day 5: Binary Boarding
# <ryc> 2021

def inputdata( ):
    stream = open( 'day_05_2020.input' )
    data = [ line[ : -1 ] for line in stream ]
    stream.close( )
    return data

def seat_id( code ):
    decimal = 0
    binary_split = [ 0 if char =='F' or char == 'L' else 1 for char in code ]
    for bit in binary_split:
        decimal *= 2
        decimal += bit
    return decimal

def searching( codes ):
    for index in range( len( codes ) - 1 ):
        if codes[ index ] + 2 == codes[ index + 1 ]:
            return codes[ index ] + 1

if __name__ == '__main__':
    print( '\n5: Binary Boarding' )
    data = inputdata( )
    seat_ids = [ seat_id( code ) for code in data  ]
    seat_ids.sort()
    print( '\nHighest seat id =', seat_ids[ -1 ] )
    print( '\nSeat_id loss =', searching( seat_ids ) )
