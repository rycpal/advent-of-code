# Day 16: Ticket Translation
# <ryc> 2021

import re

def inputdata():
    fields = dict()
    our_ticket = list()
    nearby_tickets = list()
    with open('day_16_2020.input') as stream:
        line = stream.readline()
        while len(line) != 1:
            tmp = re.findall('^(.*): (\d+)-(\d+) or (\d+)-(\d+)',line)
            fields[tmp[0][0]] = [ int(n) for n in tmp[0][1:] ]
            line = stream.readline()
        line = stream.readline()
        line = stream.readline()
        our_ticket = [ int(n) for n in re.findall('\d+',line) ]
        line = stream.readline()
        line = stream.readline()
        line = stream.readline()
        while line:
            nearby_tickets.append([ int(n) for n in re.findall('\d+',line) ])
            line = stream.readline()
    return fields, our_ticket, nearby_tickets

def scanning_error(fields, nearby_tickets):
    ranges = list()
    error = 0
    for field in fields.values():
        ranges.append(field[:2])
        ranges.append(field[2:])
    for ticket in nearby_tickets:
        for item in ticket:
            for minor, mayor in ranges:
                if minor <= item <= mayor:
                    break
            else:
                error += item
    return error

def searching(fields, our_ticket, nearby_tickets):
    # remove error tickets
    ranges = list()
    for field in fields.values():
        ranges.append(field[:2])
        ranges.append(field[2:])
    error = set()
    for ti, ticket in enumerate(nearby_tickets):
        for item in ticket:
            for minor, mayor in ranges:
                if minor <= item <= mayor:
                    break
            else:
                error.add(ti)
    error = list(error)
    error.sort(reverse=True)
    for ti in error:
        nearby_tickets.pop(ti)
    # add our ticket
    nearby_tickets.append(our_ticket)
    # search candidates
    columns = [ list() for co in our_ticket ]
    for ro in range(len(nearby_tickets)):
        for co in range(len(columns)):
            columns[co].append(nearby_tickets[ro][co])
    candidates = { key:list() for key in fields.keys() }
    for key, ranges in fields.items():
        for co in range(len(columns)):
            for value in columns[co]:
                if not(ranges[0] <= value <= ranges[1] or ranges[2] <= value <= ranges[3]):
                    break
            else:
                candidates[key].append(co)
    # reduce candidates
    while candidates != dict():
        column = None
        for key in candidates.keys():
            if len(candidates[key]) == 1:
                column = candidates[key].pop()
                fields[key].append(column)
                del candidates[key]
                break
        for candidate in candidates.values():
            candidate.remove(column)
    # departure fields
    value = 1
    for name in fields.keys():
        if name.find('departure') >= 0:
            value *= our_ticket[fields[name][4]]
    return value

if __name__ == '__main__':
    print('\n16: Ticket Translation')
    fields, our_ticket, nearby_tickets = inputdata()
    print('\nerror =',scanning_error(fields, nearby_tickets))
    print("\ndeparture fields =",searching(fields, our_ticket, nearby_tickets))
