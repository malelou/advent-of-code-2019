from math import floor

def parse(lines):
    ans = []
    for line in lines:
        if line:
            ans.append(int(line))
    return ans

def solve(data):
    total = 0 
    for num in data:
        total += calculateFuel(num)
    return total

def calculateFuel(value):
    temp = floor(value / 3) - 2
    if(temp > 0):
        return temp + calculateFuel(temp)
    else: 
        return 0
    