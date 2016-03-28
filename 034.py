def sumDigitFactorials(num):
    factorials = [1] * 10
    fac = 1
    for i in xrange(2, 10):
        fac *= i
        factorials[i] = fac
    res = []
    for n in xrange(10, num):
        temp = n
        sumFactorials = 0
        while temp > 0:
            sumFactorials += factorials[temp%10]
            temp /= 10
        if sumFactorials == n:
           res.append(n)
    print res
    return sum(res)

print sumDigitFactorials(10**5)
