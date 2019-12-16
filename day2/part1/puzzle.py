from math import floor

def parse(lines):
    for line in lines:
        if line:
            return [int(x) for x in lines[0].split(',')]

def solve(data):
    i = 0
    while(i < len(data)):
        if(data[i] == 99):
            i = len(data)
        elif(data[i] == 1 and i + 3 < len(data)):
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
            i += 4
        elif(data[i] == 2 and i + 3 < len(data)):
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
            i += 4
        else:
            i += 1
    return data