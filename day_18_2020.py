# Day 18: Operation Order
# <ryc> 2021

def inputdata():
    with open('day_18_2020.input') as stream:
        data = [ line for line in stream ]
        return data

def calculate(stream, functions):
    stream = list(stream)
    stack = list()
    operators = ['(']
    while len(stream) != 0:
        token = stream.pop(0)
        if '0' <= token <= '9':
            while len(stream) != 0 and '0' <= stream[0] <= '9':
                token += stream.pop(0)
            stack.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token in functions:
            while len(operators) != 0 and functions[operators[len(operators)-1]][0] >= functions[token][0]:
                stack.append(functions[operators.pop()][1](stack.pop(),stack.pop()))
            operators.append(token)
        elif token == ')':
            token = operators.pop()
            while token != '(':
                stack.append(functions[token][1](stack.pop(),stack.pop()))
                token = operators.pop()
    token = operators.pop()
    while token != '(':
        stack.append(functions[token][1](stack.pop(),stack.pop()))
        token = operators.pop()
    return stack.pop()

def sumatory(data):
    basic = 0
    advance = 0
    functions1 = { '(': [0], '+':[1, lambda x, y: x + y], '*':[1, lambda x, y: x * y]  }
    functions2 = { '(': [0], '+':[2, lambda x, y: x + y], '*':[1, lambda x, y: x * y]  }
    for row in data:
        basic += calculate(row, functions1)
        advance += calculate(row, functions2)
    return basic, advance

if __name__ == '__main__':
    print('\n18: Operation Order')
    data = inputdata()
    basic, advance = sumatory(data)
    print('\n basic sumatory =', basic)
    print('\n advance sumatory =', advance)
