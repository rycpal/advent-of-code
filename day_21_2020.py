# Day 21: Allergen Assessment
# <ryc> 2021

import re

def inputdata():
    with open('day_21_2020.input') as stream:
        data = list()
        for row in stream:
            row = re.findall('\w*', row)
            index = row.index('contains')
            data.append([set(row[:index]) - {''}, set(row[(index+1):]) - {''}])
    return data

def processing(data):
    allergens = dict()
    for set_ingredients, set_allergens in data:
        for allergen in set_allergens:
            if allergen in allergens:
                allergens[allergen] &= set_ingredients
            else:
                allergens[allergen] = set_ingredients.copy()
    keys = list(allergens.keys())
    while len(keys) != 0:
        key = keys.pop(0)
        if len(allergens[key]) == 1:
            for other in keys:
                allergens[other] -= allergens[key]
            allergens[key] = allergens[key].pop()
        else:
            keys.append(key)
    count = 0
    for set_ingredients, set_allergens in data:
        for ingredient in set_ingredients:
            if ingredient not in allergens.values():
                count += 1
    keys = list(allergens.keys())
    keys.sort()
    cannonical = allergens[keys.pop(0)]
    for key in keys:
        cannonical += ',' + allergens[key]
    return count, cannonical

if __name__ == '__main__':
    print('\n21: Allergen Assessment')
    data = inputdata()
    count, cannonical = processing(data)
    print('\ncount = ', count)
    print('\ncannonical =', cannonical)
