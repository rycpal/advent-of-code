# Day 14: Docking Data
# <ryc> 2021

import re

def inputdata():
    stream = open('day_14_2020.input')
#    stream = open('input')
    data = []
    for line in stream:
        record = re.findall('(mask) = ([01X]+)|(mem)\[(\d+)\] = (\d+)',line)
        if record[0][0] == 'mask':
            maskN = 0
            maskX = 0
            maskv = 0x800000000
            maskV = []
            for char in record[0][1]:
                maskN *= 2
                maskX *= 2
                if char == 'X':
                    maskX += 1
                    maskV.insert(0,maskv)
                else:
                    maskN += int(char)
                maskv >>= 1
            data.append(['mask', maskN, maskX, maskV])
        else:
            data.append([record[0][2], int(record[0][3]), int(record[0][4])])
    stream.close()
    return data

def emulator_v1(program):
    mem = dict()
    maskN = 0
    maskX = ~ 0
    for line in program:
        if line[0] == 'mask':
            maskN = line[1]
            maskX = line[2]
        else:
            mem[line[1]] = ( line[2] & maskX ) | maskN
    value = 0
    for record in mem.values():
        value += record
    return value

def emulator_v2(program):
    mem = dict()
    maskN = 0
    maskX = ~ 0
    maskV = []
    for line in program:
        if line[0] == 'mask':
            maskN = line[1]
            maskX = line[2]
            maskV = [ 0 ]
            for i in line[3]:
                branch = []
                for j in maskV:
                    branch.append(i + j)
                maskV.extend(branch)
        else:
            base = ( line[1] | maskN ) & ~ maskX
            for offset in maskV:
                mem[base + offset] = line[2]
    value = 0
    for record in mem.values():
        value += record
    return value

if __name__ == '__main__':
    print('\n14: Docking Data')
    program = inputdata()
    print('\nemulator v1 =',emulator_v1(program))
    print('\nemulator v2 =',emulator_v2(program))
