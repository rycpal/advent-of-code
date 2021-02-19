# Day 2: Password Philosophy
# <ryc> 2021

def inputdata( ):
    stream = open( 'day_02_2020.input' )
    inputs = [ ]
    for line in stream:
        hyphen = line.find( '-' )
        space = line.find( ' ' )
        colon = line.find( ':' )
        number1 = int( line[ : hyphen ] )
        number2 = int( line[ hyphen + 1 : space ] )
        letter = line[ space + 1 : colon ]
        password = line[ colon + 2 : ]
        inputs.append( ( number1, number2, letter, password ) )
    stream.close( )
    return inputs

def policy1( inputs ):
    valid = 0
    for ( minor, mayor, letter, password ) in inputs:
        match = 0
        for char in password:
            if char == letter:
                match += 1
        if minor <= match <= mayor:
            valid += 1
    return valid

def policy2( inputs ):
    valid = 0
    for ( pos1, pos2, letter, password ) in inputs:
        if password[ pos1 - 1 ] == letter and password[ pos2 - 1 ] != letter:
            valid += 1
        elif password[ pos1 - 1 ] != letter and password[ pos2 - 1 ] == letter:
            valid += 1
    return valid

if __name__ == '__main__':
    print( '\nDay 2: Password Philosophy' )
    inputs = inputdata( )
    valid = policy1( inputs )
    print( "\npolicy 1: ", valid )
    valid = policy2( inputs )
    print( "\npolicy 2: ", valid )
