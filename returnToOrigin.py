directions = {
    'N': 1,
    'S': -1,
    'E': 1,
    'W': -1
}

def isReturnedToOrigin(s):
    trimmedString = s.strip().upper()
    xAxis = 0
    yAxis = 0
    for c in trimmedString:
        if c == 'N':
            yAxis = yAxis + 1
        if c == 'S':
            yAxis = yAxis - 1
        if c == 'E':
            xAxis = xAxis + 1
        if c == 'W':
            xAxis = xAxis - 1
    if xAxis == 0 and yAxis == 0:
        return True
    else:
        return False


inputString = 'abcdewss'
print(isReturnedToOrigin(inputString))