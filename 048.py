def selfPowers(num):
    sum = 0
    for i in xrange(1, num+1):
        sum += i**i
    return sum%(10**10)

def selfPowers2(num):
    sum = 0
    for i in xrange(1, num+1):
        power10 = 1
        for j in xrange(i):
            power10 = power10*i%(10**10)
        sum += power10
    return sum%(10**10)

print selfPowers2(1000)