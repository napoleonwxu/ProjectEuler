def nstPrime(n):
    primes = [2]
    count = 1
    num = 3
    while count < n:
        isPrime = True
        for prime in primes:
            if num%prime == 0:
                isPrime = False
                break
        if isPrime is True:
            primes.append(num)
            count += 1
        num += 2
    #print primes
    return primes[-1]

print nstPrime(10001)