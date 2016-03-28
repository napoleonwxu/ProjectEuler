def specialPythagoreanTriplet():
    for a in xrange(1, 333):
        for b in xrange(a+1, 500):
            c = 1000 - a - b
            if a*a + b*b == c*c:
                print a, '+', b, '+', c, '=', 1000
                print c*c, '=', a*a, '+', b*b
                print a, '*', b, '*', c, '=', a*b*c

specialPythagoreanTriplet()