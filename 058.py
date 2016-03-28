def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def spiralPrimes(rate):
    length = 1
    numPrimes = 0
    n = 1
    d = 2
    while True:
        for i in xrange(4):
            n += d
            if isPrime(n):
                numPrimes += 1
        length += 2
        if float(numPrimes)/(2*length+1) < rate:
            #print n
            return length
        d += 2

print spiralPrimes(0.1)