def power2():
    isPower2 = [False] * (6*100+1)
    count = 0
    for d in xrange(1, 6+1):
        for i in xrange(d*2, d*100+1, d):
            if isPower2[i] == True:
                count += 1
            else:
                isPower2[i] = True
    return count

def power3():
    isPower3 = [False] * (4*100+1)
    count = 0
    for d in xrange(1, 4+1):
        for i in xrange(d*2, d*100+1, d):
            if isPower3[i] == True:
                count += 1
            else:
                isPower3[i] = True
    return count

def power5_6_7_10():
    isPower = [False] * (2*100+1)
    count = 0
    for d in xrange(1, 2+1):
        for i in xrange(d*2, d*100+1, d):
            if isPower[i] == True:
                count += 1
            else:
                isPower[i] = True
    return count

#print power2(), power3(), power5_6_7_10()
print 99*99 - power2() - power3() - power5_6_7_10()*4
