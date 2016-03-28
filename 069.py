def primesBelowNum(num):
    isPrime = [True]*num
    isPrime[0] = isPrime[1] = False
    for n in xrange(4, num, 2):
        isPrime[n] = False
    n = 3
    while n*n <= num:
        p = n * n
        n2 = n + n
        while p < num:
            isPrime[p] = False
            p += n2
        n += 2
    primes = []
    for n in xrange(num):
        if isPrime[n]:
            primes.append(n)
    return primes

def phiFunction(primes, n):
    if n < 2:
        return
    phi = n
    for prime in primes:
        if prime > n:
            break
        if n%prime == 0:
            phi *= 1 - 1.0/prime
    return int(phi)

def totientMaximum(num):
    primes = primesBelowNum(num+1)
    res_rate = 0
    for n in xrange(2, num+1, 2):   #even only
        #print n
        phi = phiFunction(primes, n)
        rate = float(n)/phi
        if rate > res_rate:
            res_n = n
            res_phi = phi
            res_rate = rate
    print res_n, res_phi, res_rate
    return res_n

print totientMaximum(10**4) # slow !!!
#http://www.kylen314.com/archives/4943  :  2*3*5*7*11*13*17 = 510510