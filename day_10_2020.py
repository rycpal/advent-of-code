# Day 10: Adapter Array
# <ryc> 2021

def inputdata():
    stream = open('day_10_2020.input')
    data = [ int(number) for number in stream ]
    stream.close()
    return data

def difference_rates(data):
    differences = [0,0,0,0]
    for index in range(len(data)-1):
        differences[data[index+1]-data[index]] += 1
    return differences

def roads(n,previus):
    if len(previus)==0:
        previus.extend([1,1,2])
    if n >= len(previus):
        for i in range(len(previus),n+1):
            previus.append(previus[i-3]+previus[i-2]+previus[i-1])
    return previus[n]

def get_ways(data):
    count_one = 0
    ways = 1
    previus = list()
    for index in range(len(data)-1):
        if data[index+1]-data[index] == 1:
            count_one += 1
        else: # data[index+1]-data[index] == 3
            ways *= roads(count_one,previus)
            count_one = 0
    return ways

if __name__ == '__main__':
    print('\n10: Adapter Array')
    data = inputdata()
    data.append(0)
    data.sort()
    data.append(data[-1]+3)
    differences = difference_rates(data)
    print('\ndifferences rates =',differences)
    print('\nd1*d3 =',differences[1]*differences[3])
    print('\nways =',get_ways(data))
