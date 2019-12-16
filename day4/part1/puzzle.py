from math import floor

def solve(data):
    validValues = []
    for value in range(data[0], data[1] + 1):
        strValue = str(value)
        i = 1
        hasDouble = False
        hasDecrease = False
        while(i < len(strValue)):
            if(strValue[i] < strValue[i - 1]):
                hasDecrease = True
            if(strValue[i] == strValue[i - 1]):
                hasDouble = True            
            i += 1
        if(hasDouble and not hasDecrease): 
            validValues.append(value)
    return len(validValues)