# Day 3: Perfectly Spherical Houses in a Vacuum
# <ryc> 2021

def inputdata():
    with open('day_03_2015.input') as stream:
        data = stream.readline()
    return data

def get_houses(data):
    houses = set()
    location = 0+0j
    houses.add(location)
    for step in data:
        if step == '^':
            location += 1j
        elif step == '>':
            location += 1+0j
        elif step == 'v':
            location += -1j
        elif step == '<':
            location += -1+0j
        houses.add(location)
    return houses

def get_houses_two(data):
    steps_santa = data[0::2]
    steps_robo = data[1::2]
    houses = get_houses(steps_santa)
    houses |= get_houses(steps_robo)
    return houses

def run():
    print('\nDay 3: Perfectly Spherical Houses in a Vacuum')
    data = inputdata( )
    print('\nhouses =', len(get_houses(data)))
    print('\nhouses =', len(get_houses_two(data)))

if __name__ == '__main__':
    run()
