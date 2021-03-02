# Day 15: Rambunctious Recitatium
# <ryc> 2021

def searching(data,last):
    now = 0
    index = 0
    previous = dict()
    for number in data[:-1]:
        previous[number] = index
        index +=1
    now = data[-1]
    while index + 1 < last:
        new = 0 if now not in previous else index - previous[now]
        previous[now] = index
        index += 1
        now = new
    return now

if __name__ == '__main__':
    print('\n15: Rambunctious Recitatium')
    data = [7, 12, 1, 0, 16, 2]
    last = 2020
    print(f'\nsearching {last}th for {data} = {searching(data,last)}')
    last = 30000000
    print(f'\nsearching {last}th for {data} = {searching(data,last)}')
