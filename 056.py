def powerfulDigitSum(num):
    maximum = 0
    aa = bb = 0
    for a in xrange(num):
        for b in xrange(num):
            s = sum([int(d) for d in str(a**b)])
            if s > maximum:
                maximum = s
                aa, bb = a, b
    print aa, bb
    return maximum

print powerfulDigitSum(100)