def primesBelowNum(num):
    isPrime = [True] * num
    isPrime[0] = isPrime[1] = False
    for i in xrange(4, num, 2):
        isPrime[i] = False
    i = 3
    while i*i < num:
        p = i*i
        i2 = i + i
        while p < num:
            isPrime[p] = False
            p += i2
        i += 2
    primes = []
    for i in xrange(num):
        if isPrime[i] == True:
            primes.append(i)
    return primes

def consecutivePrimeSum(num):
    primes = primesBelowNum(num)
    primeSum = []
    pSum = primes[0]
    i = 1
    while pSum < num:
        primeSum.append(pSum)
        pSum += primes[i]
        i += 1
    l = len(primeSum)
    #print primeSum
    #print l
    n = 0
    while True:
        if primeSum[l-n-1] in primes:
            return l-n, primeSum[l-n-1]
        for i in xrange(n):
            p = primeSum[l-i-1]-primeSum[n-i-1]
            if p in primes:
                return l-n, p
        n += 1

print consecutivePrimeSum(10**6)
