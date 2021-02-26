# Day 11: Seating System
# <ryc> 2021

def inputdata():
    stream = open('day_11_2020.input')
    data = [ line[:-1] for line in stream ]
    stream.close()
    return data

def initial_room(data):
    # room [active <-> noactive]
    room = [list(), list()]
    for row in data:
        room[0].append(list(row))
        room[1].append([ '.' if column=='.' else '#' for column in row ])
    return room

def search_vector(data,position,items,vector,limits):
    limits[0] = limits[0] if limits[0] >= 0 else 0
    limits[2] = limits[2] if limits[2] < len(data) else len(data) - 1
    limits[1] = limits[1] if limits[1] >= 0 else 0
    limits[3] = limits[3] if limits[3] < len(data[0]) else len(data[0]) - 1
    position[0] += vector[0]
    position[1] += vector[1]
    while limits[0] <= position[0] <= limits[2] and limits[1] <= position[1] <= limits[3]:
        if data[position[0]][position[1]] in items:
            return data[position[0]][position[1]]
        position[0] += vector[0]
        position[1] += vector[1]

def counted_seats(data):
    count = 0
    for row in range(len(data)):
        for column in range(len(data[0])):
            if data[row][column] == '#':
                count += 1
    return count

def searching_one(data):
    room = initial_room(data)
    no = { 0:1, 1:0 }
    active = 1
    while room[0] != room[1]:
        for row in range(len(data)):
            for column in range(len(data[0])):
                around = list()
                vectors = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
                limits = [row - 1, column -1, row + 1, column + 1]
                around = [ search_vector(room[active], [row, column], ['L', '#'], v, limits) for v in vectors ]
                around = len([ x for x in around if x == '#' ])
                if room[active][row][column] == 'L' and around == 0:
                    room[no[active]][row][column] = '#'
                elif room[active][row][column] == '#' and around >= 4:
                    room[no[active]][row][column] = 'L'
                else:
                    room[no[active]][row][column] = room[active][row][column]
        active = no[active]
    return counted_seats(room[0])

def searching_two(data):
    room = initial_room(data)
    no = { 0:1, 1:0 }
    active = 1
    while room[0] != room[1]:
        for row in range(len(data)):
            for column in range(len(data[0])):
                around = list()
                vectors = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
                limits = [0, 0, len(data) - 1, len(data[0]) - 1]
                around = [ search_vector(room[active], [row, column], ['L', '#'], v, limits) for v in vectors ]
                around = len([ x for x in around if x == '#' ])
                if room[active][row][column] == 'L' and around == 0:
                    room[no[active]][row][column] = '#'
                elif room[active][row][column] == '#' and around >= 5:
                    room[no[active]][row][column] = 'L'
                else:
                    room[no[active]][row][column] = room[active][row][column]
        active = no[active]
    return counted_seats(room[0])

if __name__ == '__main__':
    print('\n11: Seating System')
    data = inputdata()
    print('\nsearching occupied seats one =',searching_one(data))
    print('\nsearching occupied seats two =',searching_two(data))
