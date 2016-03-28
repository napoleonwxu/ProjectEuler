import math

def isPentagon(pn):
    n = (math.sqrt(24*pn+1)+1)/6
    if n == int(n):
        return True
    return False

def pentagonNumbers():
    j = 2
    while True:
        pj = j*(3*j-1)/2
        for k in xrange(1, j):
            pk = k*(3*k-1)/2
            if isPentagon(pj+pk) and isPentagon(pj-pk):
                print j, pj, k, pk
                return pj-pk
        j += 1

print pentagonNumbers()