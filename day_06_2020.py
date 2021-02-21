# Day 6: Custom Customs
# <ryc> 2021

def inputdata( ):
    stream = open('day_06_2020.input')
    data = [ ]
    record = [ ]
    for line in stream:
        if len(line) == 1:
            data.append(record)
            record = [ ]
        else:
            record.append(line[ : -1 ])
    data.append(record)
    stream.close()
    return data

def processing( groups ):
    count_union = 0
    count_intersection = 0
    universe = { chr(i) for i in range(ord('a'),ord('z')+1) }
    for group in groups:
        union = set()
        intersection = universe.copy()
        for person in group:
            answer = set(person)
            union |= answer
            intersection &= answer
        count_union += len(union)
        count_intersection += len(intersection)
    return ( count_union, count_intersection )

if __name__ == '__main__':
    print('\nDay 6: Custom Customs')
    groups = inputdata()
    ( count_union, count_intersection ) = processing(groups)
    print('\nCount union=', count_union)
    print('\nCount intersection',count_intersection)
