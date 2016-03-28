def summationBelowPrimes(num):  #slow !!!
    primes = [2]
    sum = 2
    for n in xrange(3, num, 2):
        isPrime = True
        for prime in primes:
            if n%prime == 0:
                isPrime = False
                break
        if isPrime == True:
            #print n
            primes.append(n)
            sum += n
    return sum

def summationPrimesBelowNum(num):
    primes = [True]*num
    '''
    primes[0] = primes[1] = False
    for n in xrange(4, num, 2):
        primes[n] = False
    '''
    n = 3
    while n*n < num:
        if primes[n] == True:
            i = n * n
            nn = 2 * n
            while i < num:
                primes[i] = False
                i += nn
        n += 2
    sum = 2
    for n in xrange(3, num, 2):
        if primes[n] == True:
            sum += n
    return sum

print summationPrimesBelowNum(2000000)