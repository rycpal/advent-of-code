# 24: Lobby Layout
# <ryc> 2021

def inputdata():
    with open('day_24_2020.input') as stream:
        data = stream.readlines()
    return data

def flip_on(tile, blacks):
    index = 0
    identifier = 0
    while tile[index] != '\n':
        if tile[index] == 'e':
            identifier += 2
        elif tile[index] == 'w':
            identifier -= 2
        elif tile[index] == 's':
            index += 1
            if tile[index] == 'e':
                identifier += 1-2j
            else:
                identifier += -1-2j
        else:
            index += 1
            if tile[index] == 'w':
                identifier += -1+2j
            else:
                identifier += 1+2j
        index += 1
    if identifier in blacks:
        blacks.remove(identifier)
    else:
        blacks.add(identifier)
    return blacks

def day0(data):
    blacks = set()
    for tile in data:
        flip_on(tile, blacks)
    return blacks

def next_day(blacks):
    candidates = dict()
    for tile in blacks:
        candidates[tile] = 0
    for tile in blacks:
        for delta in [2, 1-2j, -1-2j, -2, -1+2j, 1+2j]:
            adjacent = tile + delta
            candidates[adjacent] = 1 if adjacent not in candidates else candidates[adjacent] + 1
    blacks_flip_on = set()
    whites_flip_on = set()
    for candidate in candidates.keys():
        if candidate in blacks and (candidates[candidate] == 0 or candidates[candidate] > 2):
            blacks_flip_on.add(candidate)
        elif candidate not in blacks and candidates[candidate] == 2:
            whites_flip_on.add(candidate)
    for tile in blacks_flip_on:
        blacks.remove(tile)
    for tile in whites_flip_on:
        blacks.add(tile)
    return blacks

def day100(blacks):
    for _ in range(100):
        next_day(blacks)
    return blacks

if __name__ == '__main__':
    print('\n24: Lobby Layout')
    data = inputdata()
    blacks = day0(data)
    print('\nblack tiles on day 0:', len(blacks))
    blacks = day100(blacks)
    print('\nblack tiles on day 100:', len(blacks))
