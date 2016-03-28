def permutedMultiples(mul):
    d = 0
    while True:
        for n in xrange(10**d+2, 10**(d+1)/mul):
            strN = sorted(str(n))
            flag = True
            for i in xrange(2, mul+1):
                if sorted(str(i*n)) != strN:
                    flag = False
                    break
            if flag == True:
                return n
        d += 1

res = permutedMultiples(6)
for i in xrange(1, 7):
    print i*res