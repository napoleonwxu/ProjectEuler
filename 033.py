def digitCancellingFractions():
    common = []
    simple = []
    for a in xrange(1, 5):
        for b in xrange(a+1, 10):
            for c in xrange(1, 10):
                if float(10*a+b)/(10*b+c) == float(a)/c:
                    common.append(str(10*a+b)+'/'+str(10*b+c))
                    simple.append(str(a)+'/'+str(c))
    print common
    print simple

digitCancellingFractions()