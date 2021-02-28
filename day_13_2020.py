# Day 13: Shuttle Search
# <ryc> 2021

import re

def inputdata():
    stream = open('day_13_2020.input')
    data = [ line for line in stream ]
    time = int(data[0])
    bus = re.findall('\d+',data[1])
    bus = [ int(item) for item in bus ]
    vector = re.findall('(\d+|x)',data[1])
    vector = [ [ 1, i*(-1), int(vector[i]) ] for i in range(len(vector)) if vector[i] != 'x' ]
    stream.close()
    return time, bus, vector

def searching(time,bus):
    minutes = [ time % b for b in bus ]
    minutes = [ abs(b - time % b) for b in bus ]
    minor = min(minutes)
    index = minutes.index(minor)
    return minor * bus[index]

def normalize(v):
    v_n = v.copy()
    v_n[0] %= v_n[2]
    v_n[1] %= v_n[2]
    r = v_n[1]
    while r % v_n[0] != 0:
        r += v_n[2]
    v_n[1] = int(r / v_n[0])
    v_n[0] = 1
    return v_n

def congruence(x,y):
    x_n = normalize(x)
    y_n = normalize(y)
    x_ny_n = normalize([x_n[2], y_n[1] - x_n[1], y_n[2]])
    return [1, x_n[1] + x_n[2]*x_ny_n[1], x_n[2]*y_n[2]]

def congruence_multiple(vector):
    v_c = vector[0]
    for i in range(1,len(vector)):
        v_c = congruence(v_c,vector[i])
    return v_c

if __name__ == '__main__':
    print('\n13: Shuttle Search')
    time, bus, vector = inputdata()
    print('\nsearching =',searching(time, bus))
    print('\ncongruence =',congruence_multiple(vector)[1])
