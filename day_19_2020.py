# Day 19: Monster Messages
# <ryc> 2021

def inputdata():
    with open('day_19_2020.input') as stream:
        data = [ line for line in stream ]
        grammar = dict()
        line = data.pop(0)
        while len(line) != 1:
            line = line.split()
            key = line.pop(0)[:-1]
            extends = [list()]
            index = 0
            for item in line:
                if item == '|':
                    index += 1
                    extends.append(list())
                else:
                    extends[index].append( item if item[0] != '"' else item[1:-1] )
            grammar[key] = extends
            line = data.pop(0)
        return grammar, data

def validate(line, grammar, first = '0'):
    ptr = 0
    stack = list()
    stack.append([[first], ptr])
    while len(stack) != 0:
        tail, ptr = stack.pop()
        if len(tail) == 0:
            if line[ptr] == '\n':
                return True
        else:
            head = tail.pop(0)
            if head == line[ptr]:
                ptr += 1
                stack.append([tail, ptr])
            elif head in grammar.keys():
                for option in grammar[head]:
                    stack.append([option + tail, ptr])
    else:
        return False

def run(grammar, data):
    count = 0
    for line in data:
        if validate(line,grammar) == True:
            count += 1
    return count

if __name__ == '__main__':
    print('\n19: Monster Messages')
    grammar, data = inputdata()
    print('\nvalid lines =', run(grammar, data))
    grammar['8'] = [['42', '8p' ]]
    grammar['8p'] = [['8'], []]
    grammar['11'] = [['42', '11p']]
    grammar['11p'] = [['31'], ['11', '31']]
    print('\nmodified grammar, valid lines', run(grammar, data))
