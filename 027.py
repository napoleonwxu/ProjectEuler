def primesBelowN(n):
    isPrimes = [True] * n
    isPrimes[0] = isPrimes[1] = False
    for i in xrange(4, n, 2):
        isPrimes[i] = False
    i = 3
    while i*i < n:
        j = i * i
        i2 = i + i
        while j < n:
            isPrimes[j] = False
            j += i2
        i += 2
    primes = []
    for i in xrange(2, n):
        if isPrimes[i] == True:
            primes.append(i)
    return primes

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    return True

def quadraticPrimes(a, b):
    num = 0
    n = 0
    while isPrime(n*n+a*n+b):
        num += 1
        n += 1
    return num

def quadraticPrimesBelowN(n):
    primes = primesBelowN(n)
    max_a = max_b = 0
    max_num = 0
    if n%2 == 0:
        start = 1 - n
    else:
        start = 2 - n
    for i in xrange(1, len(primes)):    # drop 2
        b = primes[i]
        for a in xrange(start, n, 2):   # a is odd
            num = quadraticPrimes(a, b)
            #print b, a, num
            if num > max_num:
                max_num = num
                max_a, max_b = a, b
    print 'a:', max_a, 'b:', max_b, 'max_num:', max_num
    return max_a * max_b

print quadraticPrimesBelowN(1000)