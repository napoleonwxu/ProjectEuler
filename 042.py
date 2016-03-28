import math

def editFile(fileName):
    f = open(fileName)
    for line in f:
        strs = line.strip('"').split('","')
    return strs

def codedTriangleNumbers(fileName):
    count = 0
    for s in editFile(fileName):
        code = 0
        for ch in s:
            code += ord(ch) - ord('A') + 1
        n = math.sqrt(2*code+0.25) - 0.5
        if n == int(n):
            count += 1
    return count

fileName = 'p042_words.txt'
print codedTriangleNumbers(fileName)