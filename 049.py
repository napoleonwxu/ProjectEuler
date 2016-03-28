def fourDigitsPrimes():
    isPrime = [True] * (10**4)
    isPrime[0] = isPrime[1] = False
    for i in xrange(4, len(isPrime), 2):
        isPrime[i] = False
    i = 3
    while i*i < len(isPrime):
        p = i * i
        i2 = i + i
        while p < len(isPrime):
            isPrime[p] = False
            p += i2
        i += 2
    primes = []
    for i in xrange(10**3, 10**4):
        if isPrime[i]:
            primes.append(i)
    #print len(primes)
    return primes

def primePermutations():
    res = []
    primes = fourDigitsPrimes()
    #print primes
    for i in xrange(len(primes)):
        for j in xrange(i+1, len(primes)):
            p = primes[j] + primes[j] - primes[i]
            if set(str(primes[i])) == set(str(primes[j])) == set(str(p)) and p in primes:
                res.append(str(primes[i])+str(primes[j])+str(p))
    return res
print primePermutations()
