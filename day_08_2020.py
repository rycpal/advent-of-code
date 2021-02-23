# Day 8: Handhelp Halting
# <ryc> 2021

def inputdata():
    stream = open('day_08_2020.input')
    program = [ line for line in stream ]
    stream.close()
    return program

def processing(program):
    accumulator = 0
    pointer = 0
    exit = False
    while pointer < len(program) and not exit:
        instruction = program[pointer][0:3]
        offset = int(program[pointer][4:-1])
        #print(pointer, program[pointer][:-1],instruction,offset,accumulator)
        if instruction == 'nop':
            program[pointer] = 'rep +0 '
            pointer += 1
        elif instruction == 'acc':
            accumulator += offset
            program[pointer] = 'rep +0 '
            pointer += 1
        elif instruction == 'jmp':
            program[pointer] = 'rep +0 '
            pointer += offset
        elif instruction == 'rep':
            exit = True
    return accumulator,pointer

def reparing(program):
    change = { 'nop':'jmp' , 'jmp':'nop' }
    for focus in range(len(program)):
        instruction = program[focus][0:3]
        offset = program[focus][4:]
        if instruction in change:
            program_copy = program.copy()
            program_copy[focus] = change[instruction] + offset
            accumulator,pointer = processing(program_copy)
            if pointer == len(program):
                return accumulator

if __name__ == '__main__':
    print('\n8: Handhelp Halting')
    program = inputdata()
    accumulator,pointer = processing(program)
    print('\nAccumulator =',accumulator)
    program = inputdata()
    print('\nAccumulator reparing =',reparing(program))
