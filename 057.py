def squareRootConvergents(num):
    count = 0
    nu, de = 2, 3
    for i in xrange(num):
        if len(str(nu)) > len(str(de)):
            count += 1
        nu, de = 2*de+nu, de+nu
    return count

print squareRootConvergents(1000)
