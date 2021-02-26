# Day 12: Rain Risk
# <ryc> 2021

def inputdata():
    stream = open('day_12_2020.input')
    data = [ (line[0], int(line[1:])) for line in stream ]
    stream.close()
    return data

def navigation(data,position,vector,relative=False):
    cardinal = {'E':1+0j, 'S':-1j, 'W':-1+0j, 'N':1j}
    sign = {'R':1, 'L':-1}
    traslate = ['E', 'S', 'W', 'N']
    for action, value in data:
        if action in cardinal:
            if relative:
                vector += cardinal[action] * value
            else:
                position += cardinal[action] * value
        elif action in sign:
            vector *= cardinal[traslate[(sign[action] * int(value / 90) ) % 4]]
        else:
            position += vector * value
    return position

if __name__ == '__main__':
    print('\n12: Rain Risk')
    data = inputdata()
    position = navigation(data,0j,1+0j)
    print('\nManhattan distance =',int(abs(position.real) + abs(position.imag)))
    print(position)
    position = navigation(data,0j,10+1j,relative=True)
    print('\nManhattan distance, relative navigation =',int(abs(position.real) + abs(position.imag)))
    print(position)
