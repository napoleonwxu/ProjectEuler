def champernowneConstant():
    i = 0
    strs = ''
    res = 1
    while len(strs) <= 10**6:
        strs += str(i)
        i += 1
    for i in xrange(7):
        print int(strs[10**i])
        res *= int(strs[10**i])
    return res

print champernowneConstant()