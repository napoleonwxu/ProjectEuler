def isPrime(num):
    if num == 2:
        return True
    if num%2 == 0:
        return False
    i = 3
    while i*i < num:
        if num%i == 0:
            return False
        i += 2
    return True

def yieldPandigitalMaxtoMin(digits):
    if len(digits) == 1:
        yield digits[0]
    for i in xrange(len(digits)):
        for d in yieldPandigitalMaxtoMin(digits[:i]+digits[i+1:]):
            yield digits[i]*(10**(len(digits)-1)) + d

def maxPandigitalPrime():
    for n in xrange(7, 0, -1):  #1+2+...+9=45, num%3==0; 1+2+...+8=36, num%3==0; 1+2+...+7=28
        digits = [i for i in xrange(n, 0, -1)]
        for digit in yieldPandigitalMaxtoMin(digits):
            if isPrime(digit):
                return digit

print maxPandigitalPrime()