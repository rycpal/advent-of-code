# Day 23: Crab Cups
# <ryc> 2021

def inputdata(label, n_cups):
#   data = [first, next_1, next_2, ..., first ]
    assert n_cups >= len(label)
    LEN = len(label)
    data = [ x for x in range(1,n_cups+2)]
    data[0] = int(label[0])
    for index in range(LEN-1):
        data[int(label[index])] = int(label[index+1])
    if n_cups > LEN:
        data[int(label[LEN-1])] = LEN + 1
        data[-1] = data[0]
    else:
        data[int(label[LEN-1])] = data[0]
    return data

def playing(data, n_rounds):
    current = data[0]
    CUPS = len(data) - 1
    pick_up = [1, 2, 3]
    for _ in range(n_rounds):
        pick_up[0] = data[current]
        pick_up[1] = data[pick_up[0]]
        pick_up[2] = data[pick_up[1]]
        destination = CUPS if current == 1 else current - 1
        while destination in pick_up:
            destination = CUPS if destination == 1 else destination - 1
        data[current] = data[pick_up[2]]
        data[pick_up[2]] = data[destination]
        data[destination] = pick_up[0]
        current = data[current]
    data[0] = current
    return data

def outputdata1(data):
    output = ''
    current = 1
    for _ in range(8):
        output += str(data[current])
        current = data[current]
    return output

def outputdata2(data):
    output = 1
    current = 1
    for _ in range(2):
        output *= data[current]
        current = data[current]
    return output

if __name__ == '__main__':
    print('\n23: Crab Cups')
    label = '871369452'
    data = inputdata(label, 9)
    print('\n9 cups 100 rounds:', outputdata1(playing(data, 100)))
    data = inputdata(label, 1000000)
    print('\n1000000 cups 10000000 rounds:', outputdata2(playing(data, 10000000)))
