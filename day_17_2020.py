# Day 17: Conway Cubes
# <ryc> 2021

class ConwayCube:

    def __set_active(self, coord):
        x, y, z = coord
        if z not in self.__active_cubes:
            self.__active_cubes[z] = dict()
        if y not in self.__active_cubes[z]:
            self.__active_cubes[z][y] = set()
        if x not in self.__active_cubes[z][y]:
            self.__active_cubes[z][y].add(x)

    def __init__(self, array):
        self.__active_cubes = dict()
        for coord in array:
            self.__set_active(coord)

    def __is_active(self, coord):
        x, y, z = coord
        if z not in self.__active_cubes:
            return False
        if y not in self.__active_cubes[z]:
            return False
        if x in self.__active_cubes[z][y]:
            return True
        else:
            return False

    def run(self):
        candidates = dict()
        for z, zdict in self.__active_cubes.items():
            for y, ysets in zdict.items():
                for x in ysets:
                    neighbors = [ (i, j, k) for k in [z-1, z, z+1] for j in [y-1, y, y+1] for i in [x-1, x, x+1] if i != x or j != y or k != z ]
                    for key in neighbors:
                        if key in candidates:
                            candidates[key] += 1
                        else:
                            candidates[key] = 1
        actives = set()
        for coord, count in candidates.items():
            if 2 <= count <= 3 and self.__is_active(coord):
                actives.add(coord)
            elif count == 3 and not self.__is_active(coord):
                actives.add(coord)
        self.__active_cubes = dict()
        for coord in actives:
            self.__set_active(coord)

    def get_actives(self):
        actives = 0
        for z in self.__active_cubes.values():
            for y in z.values():
                actives += len(y)
        return actives

def inputdata(coord):
    x, y, z, w = coord
    with open('day_17_2020.input') as stream:
        data = [ line[:-1] for line in stream ]
        array_cube = list()
        array_hypercube = list()
        for j, line  in enumerate(data):
            for i, char in enumerate(line):
                if char == '#':
                    array_cube.append((i+x, j+y, z))
                    array_hypercube.append((i+x, j+y, z, w))
        return array_cube, array_hypercube

class ConwayHypercube:

    def __set_active(self, coord):
        x, y, z, w = coord
        if w not in self.__active_cubes:
            self.__active_cubes[w] = dict()
        if z not in self.__active_cubes[w]:
            self.__active_cubes[w][z] = dict()
        if y not in self.__active_cubes[w][z]:
            self.__active_cubes[w][z][y] = set()
        if x not in self.__active_cubes[w][z][y]:
            self.__active_cubes[w][z][y].add(x)

    def __init__(self, array):
        self.__active_cubes = dict()
        for coord in array:
            self.__set_active(coord)

    def __is_active(self, coord):
        x, y, z, w = coord
        if w not in self.__active_cubes:
            return False
        if z not in self.__active_cubes[w]:
            return False
        if y not in self.__active_cubes[w][z]:
            return False
        if x in self.__active_cubes[w][z][y]:
            return True
        else:
            return False

    def run(self):
        candidates = dict()
        for w, wdict in self.__active_cubes.items():
            for z, zdict in wdict.items():
                for y, ysets in zdict.items():
                    for x in ysets:
                        neighbors = [ (i,j,k,l) for l in [w-1,w,w+1] for k in [z-1,z,z+1] for j in [y-1,y,y+1] for i in [x-1,x,x+1] if i != x or j != y or k != z or l != w ]
                        for key in neighbors:
                            if key in candidates:
                                candidates[key] += 1
                            else:
                                candidates[key] = 1
        actives = set()
        for coord, count in candidates.items():
            if 2 <= count <= 3 and self.__is_active(coord):
                actives.add(coord)
            elif count == 3 and not self.__is_active(coord):
                actives.add(coord)
        self.__active_cubes = dict()
        for coord in actives:
            self.__set_active(coord)

    def get_actives(self):
        actives = 0
        for w in self.__active_cubes.values():
            for z in w.values():
                for y in z.values():
                    actives += len(y)
        return actives

def inputdata(coord):
    x, y, z, w = coord
    with open('day_17_2020.input') as stream:
        data = [ line[:-1] for line in stream ]
        array_cube = list()
        array_hypercube = list()
        for j, line  in enumerate(data):
            for i, char in enumerate(line):
                if char == '#':
                    array_cube.append((i+x, j+y, z))
                    array_hypercube.append((i+x, j+y, z, w))
        return array_cube, array_hypercube

if __name__ == '__main__':
    print('\n17: Conway Cubes')
    array_cube, array_hypercube = inputdata((-1,-1,0,0))
    cc = ConwayCube(array_cube)
    hc = ConwayHypercube(array_hypercube)
    step = 6
    for _ in range(step):
        cc.run()
        hc.run()
    print('\n actives in cube =', cc.get_actives())
    print('\n actives in hypercube =', hc.get_actives())
