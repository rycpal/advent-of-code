# Day 9: Encoding Error
# <ryc> 2021

def inputdata():
    stream = open('day_09_2020.input')
    data = [ int(number) for number in stream ]
    stream.close()
    return data

def searching(data):
    for i in range(25,len(data)):
        j = i - 25
        while j < i - 2:
            k = i - 24
            while k < i - 1 and data[i] != data[j] + data[k]:
                k += 1
            if data[i] == data[j] + data[k]:
                break
            j += 1
        else:
            return data[i]

def weakness_array(data,objetive):
    array = list()
    accumulator = 0
    for number in data:
        array.append(number)
        accumulator += number
        while accumulator > objetive:
            accumulator -= array.pop(0)
        if accumulator == objetive:
            return array

if __name__ == '__main__':
    print('\n9: Encoding Error')
    data = inputdata()
    number = searching(data)
    print('\nWeakness number =',number)
    array = weakness_array(data,number)
    min_plus_max = min(array) + max(array)
    print('\nmin + max =',min_plus_max)
