def numberSpiralDiagonals(n):
    if n < 3:
        return
    sum = 1
    num = 1
    d = 2
    for i in xrange(3, n+1, 2):
        for j in xrange(4):
            num += d
            sum += num
        d += 2
    return sum

print numberSpiralDiagonals(1001)