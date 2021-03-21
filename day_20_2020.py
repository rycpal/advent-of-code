# Day 20: Jurassic Jigsaw
# <ryc> 2021

class Tile:

    def __int(self, code):
        value = 0
        for char in code:
            value *= 2
            if char == '#':
                value += 1
        return value

    def __init__(self, frame):
        self.__frame = frame.copy()
        self.__key = 0
        top = frame[0]
        right = ''
        left = ''
        for line in frame:
            right += line[-1]
            left += line[0]
        bottom = frame[-1]
        keys = [top, right, bottom[::-1], left[::-1], top[::-1], right[::-1], bottom, left]
        self.__keys = [ self.__int(key) for key in keys ]

    def rotate(self, time=1 ):
        if self.__key < 4:
            self.__key = (self.__key + time) % 4
        else:
            self.__key = 4 + (self.__key - time) % 4
        return self.__key

    def flip(self):
        self.__key = 7 - self.__key
        return self.__key

    def get_frame(self):
        size = [len(self.__frame[0]), len(self.__frame)]
        fields = [7, 1, 4, 2, 6, 0, 5, 3]
        var = 0 if fields[self.__key] & 4 == 0 else 1
        Y = range(size[var])
        if fields[self.__key] & 2 == 0:
            Y = Y[::-1]
        X = range(size[1 if var == 0 else 0])
        if fields[self.__key] & 1 == 0:
            X = X[::-1]
        frame = list()
        for y in Y:
            row = ''
            for x in X:
                if var == 0:
                    row += self.__frame[x][y]
                else:
                    row += self.__frame[y][x]
            frame.append(row)
        return frame

    def get_keys(self):
        key = self.__key
        keys = self.__keys
        if key > 3:
            keys = keys[::-1]
            key = 7 - key
        return keys[key:4] + keys[0:key] + keys[(key+4):8] + keys[4:(key+4)]

    def connector(self, other):
        for index in range(4):
            if self.get_keys()[index] in other.get_keys():
                return self.get_keys()[index]
        else:
            return None

    def align(self, other, side=None):
        connection = self.connector(other)
        if connection == None:
            return None
        if side != None:
            self.rotate((self.get_keys().index(connection) - side) % 4)
        else:
            side = self.get_keys().index(connection)
        if other.get_keys().index(connection) < 4:
            other.flip()
        other.rotate((other.get_keys().index(connection) - side - 2) % 4)
        return side

def inputdata():
    with open('day_20_2020.input') as stream:
        data = stream.readlines()
        tiles = dict()
        while len(data) != 0:
            tile = int(data.pop(0)[5:9])
            frame = list()
            for _ in range(10):
                frame.append(data.pop(0)[:-1])
            tiles[tile] = Tile(frame)
            if len(data) != 0:
                data.pop(0)
    return tiles

def puzzle_solver(tiles, size):
    candidates = dict()
    for key in tiles.keys():
        candidates[key] = set()
    for key in tiles.keys():
        for other in tiles.keys():
            if key != other:
                if tiles[key].connector(tiles[other]) != None:
                    candidates[key].add(other)
                    candidates[other].add(key)
    puzzle = [ [ None for row in range(size[1]) ] for column in range(size[0]) ]
    keys = list(tiles.keys())
    for first in keys:
        if len(candidates[first]) == 2:
            break
    puzzle[0][0] = first
    second, third = candidates[first]
    side_second = tiles[first].align(tiles[second])
    side_third = tiles[first].align(tiles[third])
    if (side_second + 1) % 4 != side_third:
        second = third
    tiles[first].align(tiles[second], 1)
    for row in range(size[0]):
        for column in range(size[1]):
            tile = puzzle[row][column]
            for candidate in candidates[tile]:
                pos = tiles[tile].align(tiles[candidate])
                if pos == 0:
                    if puzzle[row-1][column] != candidate:
                        return None
                elif pos == 1:
                    if puzzle[row][column+1] == None:
                        puzzle[row][column+1] = candidate
                    elif puzzle[row][column+1] != candidate:
                        return None
                elif pos == 2:
                    if puzzle[row+1][column] == None:
                        puzzle[row+1][column] = candidate
                    elif puzzle[row+1][column] != candidate:
                        return None
                else:
                    if puzzle[row][column-1] != candidate:
                        return None
    return puzzle

def to_vector(array):
    vector = list()
    for row in range(len(array)):
        for column in range(len(array[0])):
            if array[row][column] == '#':
                vector.append((row, column))
    return vector

def track(monster, image):
    vector = to_vector(monster)
    count = 0
    row = len(image) - len(monster) + 1
    column = len(image[0]) - len(monster[0]) + 1
    for y in range(row):
        for x in range(column):
            for dy,dx in vector:
                if image[y+dy ][x+dx] != '#':
                    break
            else:
                count += 1
    return count

def searching(tiles, puzzle):
    _image = [ [ tiles[tile].get_frame() for tile in row ] for row in puzzle ]
    _image = [ [ [ line[1:-1]  for line in column[1:-1] ] for column in row ] for row in _image ]
    image = list()
    for k in range(12):
        for i in range(8):
            row = ''
            for j in range(12):
                row += _image[k][j][i]
            image.append(row)
    monster = Tile(['..................#.',
                    '#....##....##....###',
                    '.#..#..#..#..#..#...'])
    vectors = list()
    for _ in range(4):
        vectors.append(monster.get_frame())
        monster.rotate()
    monster.flip()
    for _ in range(4):
        vectors.append(monster.get_frame())
        monster.rotate()
    counts = [ track(_monster, image) for _monster in vectors ]
    return len(to_vector(image)) - max(counts) * len(to_vector(vectors[0]))

if __name__ == '__main__':
    print('\n20: Jurassic Jigsaw')
    tiles = inputdata()
    puzzle = puzzle_solver(tiles, [12,12])
    print('\npuzzle:',puzzle)
    print('\ncorner product =', puzzle[0][0]*puzzle[0][11]*puzzle[11][0]*puzzle[11][11])
    print('\ncount = ', searching(tiles, puzzle))
