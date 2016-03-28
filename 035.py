def primesBelowNum(num):
    isPrimes = [True] * num
    isPrimes[0] = isPrimes[1] = False
    for n in xrange(4, num, 2):
        isPrimes[n] = False
    i = 3
    while i*i < num:
        n = i * i
        ii = i + i
        while n < num:
            isPrimes[n] = False
            n += ii
        i += 2
    primes = []
    for n in xrange(num):
        if isPrimes[n] == True:
            primes.append(n)
    #print len(primes)
    return primes

def mayBeCircularPrimes(num):
    primes = primesBelowNum(num)    # [2, 3, 5, 7, 11 ... ]
    mayBeCirPrimes = []
    for prime in primes:
        if prime < 10:
            mayBeCirPrimes.append(prime)
        else:
            strPrime = str(prime)
            if '0' in strPrime or '2' in strPrime or '4' in strPrime or '5' in strPrime or '6' in strPrime or '8' in strPrime:
                continue
            mayBeCirPrimes.append(prime)
    #print len(mayBeCirPrimes)
    return mayBeCirPrimes

def circularPrimes(num):
    primes = mayBeCircularPrimes(num)
    cirPrimes = []
    for prime in primes:
        t = len(str(prime)) - 1
        flag = True
        temp = prime
        for i in xrange(t):
            temp = (10**t)*(temp%10) + temp/10
            if temp not in primes:
                flag = False
                break
        if flag:
            cirPrimes.append(prime)
    print cirPrimes
    return len(cirPrimes)

print circularPrimes(10**6)