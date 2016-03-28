def getBase(n):
    while n%2 == 0:
        n /= 2
    while n%5 == 0:
        n /= 5
    return n

def getCycle(n):
    k = 9
    i = 1
    while k%n != 0:
        k = k*10 + 9
        i += 1
    return i

def reciprocalCycles(maxNum):
    cycles = [0] * maxNum
    for n in xrange(2, maxNum):
        temp = getBase(n)
        if temp == 1:
            continue
        if temp < n:
            cycles[n] = cycles[temp]
        else:   #temp == n
            cycles[n] = getCycle(n)
    index = 1
    res = 0
    for i in xrange(1, maxNum):
        if cycles[i] > res:
            index = i
            res = cycles[index]
    return index, cycles[index]

print reciprocalCycles(1000)
