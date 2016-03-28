def sumSquareDifference(n):
    diff = 0
    for i in xrange(1, n+1):
        for j in xrange(i+1, n+1):
            diff += i*j
    return diff*2

print sumSquareDifference(100)