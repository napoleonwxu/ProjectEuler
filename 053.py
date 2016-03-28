def combinatoric(n, r):
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    res = 1
    for i in xrange(r):
        res *= n - i
    for i in xrange(r, 1, -1):
        res /= i
    return res

def combinatoricSelections():
    count = 0
    for n in xrange(1, 101):
        for r in xrange(0, n/2+1):
            if combinatoric(n, r) > 10**6:
                count += n+1-2*r
                break
    return count

print combinatoricSelections()
