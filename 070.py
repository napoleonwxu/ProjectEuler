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

def totientPermutation(num):
    primes = primesBelowNum(num/2)
    print len(primes)
    res_rate = float('inf')
    for i in xrange(len(primes)):
        for j in xrange(i, len(primes)):
            n = primes[i]*primes[j]
            if n > num:
                break
            phi = (primes[i]-1)*(primes[j]-1)
            if sorted(str(n)) == sorted(str(phi)):
                rate = float(n)/phi
                if rate < res_rate:
                    res_n = n
                    res_phi = phi
                    res_rate = rate
    print res_n, res_phi, res_rate
    return res_n

print totientPermutation(10**7)

