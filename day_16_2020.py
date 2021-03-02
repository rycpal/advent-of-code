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
    for record in fields.values():
        ranges.append(record[:2])
        ranges.append(record[2:])
    for record in nearby_tickets:
        for item in record:
            for minor, mayor in ranges:
                if minor <= item <= mayor:
                    break
            else:
                error += item
    return error

if __name__ == '__main__':
    print('\n16: Ticket Translation')
    fields, our_ticket, nearby_tickets = inputdata()
    print('\nerror =',scanning_error(fields, nearby_tickets))
