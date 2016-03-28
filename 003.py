def maxPrimeFactor(num):
    res = num
    if num%2 == 0:
        res = 2
        while num%2 == 0:
            num /= 2
    i = 3
    while num != 1:
        if num%i == 0:
            res = i
            while num%i == 0:
                num /= i
        i += 2
    '''xrange(3, 600851475143+1, 2): too large
    for i in xrange(3, num+1, 2):
        if num%i == 0:
            res = i
            while num%i == 0:
                num /= i
    '''
    return res

print maxPrimeFactor(600851475143)
'''
for i in xrange(2, 20):
    print i, maxPrimeFactor(i)
'''