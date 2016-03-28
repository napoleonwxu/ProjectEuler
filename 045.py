import math

def isTriangular(t):
    n = (math.sqrt(8*t+1)-1)/2
    if n == int(n):
        return True
    return False
def isHexagonal(h):
    n = (math.sqrt(8*h+1)+1)/4
    if n == int(n):
        return True
    return False

def isPentagonal(p):
    n = (math.sqrt(24*p+1)+1)/6
    if n == int(n):
        return True
    return False

def isTriangularPentagonalHexagonal():
    n = 143 + 1
    while True:
        t = n*(2*n-1)
        if isPentagonal(t):
            return t
        n += 1

print isTriangularPentagonalHexagonal()