# Day 7: Handy Haversacks
# <ryc> 2021

import re

def inputdata():
    stream = open('day_07_2020.input')
    data = [ line for line in stream ]
    stream.close()
    return data

def adjacent_sets(data):
    matrix = dict()
    for line in data:
        record = re.findall('(\d* *\w+ \w+) bag',line)
        key = record.pop(0)
        matrix[key] = dict()
        for item in record:
            match = re.search('(\d+) (\w+ \w+)',item)
            if match != None:
                matrix[key][match.group(2)] = int(match.group(1))
    return matrix

def get_parents(item,matrix):
    parents = set()
    for key,record in matrix.items():
        if item in record:
            parents.add(key)
    return parents

def get_ascendants(item,matrix):
    ascendants = set()
    candidates = get_parents(item,matrix)
    while len(candidates)!=0:
        key = candidates.pop()
        ascendants.add(key)
        candidates |= get_parents(key,matrix)-ascendants
    return ascendants

def count_into_bag(item,matrix,calculated=dict()):
    if item in calculated:
        return calculated[item]
    else:
        count = 0
        for descendant in matrix[item]:
                count += matrix[item][descendant] * (count_into_bag(descendant,matrix,calculated) + 1 )
        calculated[item] = count
        return count

if __name__ == '__main__':
    print('\nDay 7: Handy Haversacks')
    data = inputdata()
    matrix =adjacent_sets(data)
    print('\nCount ascendants =',len(get_ascendants('shiny gold',matrix)))
    print('\nCount descendant =',count_into_bag('shiny gold',matrix))
#    calculated = dict()
#    print('\nCount descendant =',count_into_bag('shiny gold',matrix,calculated))
#    print(calculated)
