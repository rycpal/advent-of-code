# Day 3: Toboggan Trajectory
# <ryc> 2021

def inputdata( ):
    stream = open( 'day_03_2020.input' )
    data = [ line[ : -1 ] for line in stream ] # space drop
    stream.close( )
    return data

def toboggan( data, delta_x, delta_y ):
    tree = 0
    x = 0
    y = 0
    width_pattern = len( data[ 0 ] )
    height_pattern = len( data )
    while y < height_pattern - delta_y:
        x += delta_x
        x %= width_pattern
        y += delta_y
        if data[ y ][ x ] == '#':
            tree += 1
        #print( tree ,y ,x , data[y])
    return tree

if __name__ == '__main__':
    print( '\nDay 3: Toboggan Trajectory' )
    data = inputdata( )
    scopes = ( ( 1, 1 ), ( 3, 1 ), ( 5, 1 ), ( 7, 1 ), ( 1, 2 )  )
    total = 1
    for ( right, down ) in scopes:
        tree = toboggan( data, right, down )
        total *= tree
        print( f'\nToboggan right = { right } down = { down } : { tree }' )
    print( "\nTotal =", total )
