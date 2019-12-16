from math import floor
import copy

def parse(lines):
    for line in lines:
        if line:
            return [int(x) for x in lines[0].split(',')]

def solve(data, output):
    for noun in range(0, 100):
        for verb in range(0, 100):
            if(calculate(copy.deepcopy(data), noun, verb) == output):
                return 100 * noun + verb


def calculate(data, noun, verb):
    data[1] = noun
    data[2] = verb
    i = 0
    while(i < len(data)):
        if(data[i] == 99):
            i = len(data)
        elif(data[i] == 1 and i + 3 < len(data) and data[i + 3] < len(data) and data[i + 2] < len(data) and data[i + 1] < len(data)):
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
            i += 4
        elif(data[i] == 2 and i + 3 < len(data) and data[i + 3] < len(data) and data[i + 2] < len(data) and data[i + 1] < len(data)):
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
            i += 4
        else:
            i += 1
    return data[0]