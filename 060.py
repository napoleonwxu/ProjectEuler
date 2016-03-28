def primesBelowNum(num):
    isPrimes = [True] * num
    isPrimes[0] = isPrimes[1] = False
    for n in xrange(4, num, 2):
        isPrimes[n] = False
    i = 3
    while i*i < num:
        n = i * i
        i2 = i + i
        while n < num:
            isPrimes[n] = False
            n += i2
        i += 2
    return isPrimes

'''
def isPrime(n):
    if n < 2:
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
'''
def primePairSets5(num):
    isPrimeShort = primesBelowNum(num)
    primes = []
    for n in xrange(num):
        if isPrimeShort[n]:
            primes.append(n)
    print primes
    longNum = 10**(2*len(str(num)))
    print longNum
    isPrimeLong = primesBelowNum(longNum)

    primePairs = {}
    for i in xrange(1, len(primes)):    #delete 2
        pair = []
        for j in xrange(i+1, len(primes)):
            if isPrimeLong[int(str(primes[i])+str(primes[j]))] and isPrimeLong[int(str(primes[j])+str(primes[i]))]:
                pair.append(primes[j])
        primePairs[primes[i]] = pair
        if pair:
            print primes[i], ':', pair
    '''
    for key, value in primePairs.items():
        print key, ':', value
    '''
    primePairs2 = {}
    for key, value in primePairs.items():
        pair = []
        if value:
            for i in xrange(1, len(value)):
                if value[i] in primePairs[value[0]]:
                    pair.append(value[i])
        if pair:
            primePairs2[tuple([key, value[0]])] = pair
    '''
    for key, value in primePairs2.items():
        print key, ':', value
    '''
    primePairs3 = {}
    for key, value in primePairs2.items():
        pair = []
        for i in xrange(1, len(value)):
            if value[i] in primePairs[value[0]]:
                pair.append(value[i])
        if pair:
            primePairs3[key + tuple([value[0]])] = pair

    for key, value in primePairs3.items():
        print key, ':', value

    primePairs4 = {}
    for key, value in primePairs3.items():
        pair = []
        for i in xrange(1, len(value)):
            if value[i] in primePairs[value[0]]:
                pair.append(value[i])
        if pair:
            primePairs4[key + tuple([value[0]])] = pair
    res = []
    for key, value in primePairs4.items():
        print key, ':', value
        res.append(key + tuple([value[0]]))
    return res

print primePairSets5(20000)
# 5381 5507 7877 41621 47237 Wrong