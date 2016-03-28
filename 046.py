import math

def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num%2 == 0:
        return False
    i = 3
    while i*i <= num:
        if num%i == 0:
            return False
        i += 2
    return True

def notGoldbachConjecture():
    primes = []
    odd = 3
    while True:
        #print odd
        if isPrime(odd):
            primes.append(odd)
            #print primes
        else:
            conjecture = False
            for prime in primes:
                n = math.sqrt((odd-prime)/2.0)
                if n == int(n):
                    conjecture = True
                    break
            if conjecture == False:
                return odd
        odd += 2

print notGoldbachConjecture()