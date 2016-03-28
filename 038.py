def isPandigital(numStr):
    if len(numStr) != 9:
        return False
    for i in xrange(1, 10):
        if str(i) not in numStr:
            return False
    return True

def pandigitalMultiples():
    pros = []
    multis = []
    for n in xrange(2, 10):
        mul = [i for i in xrange(1, n+1)]
        pro = []
        multi = []
        num = 1
        con = ''
        for i in mul:
            con += str(num*i)
        while len(con) < 10:
            if isPandigital(con):
                pro.append(int(con))
                multi.append(num)
            num += 1
            con = ''
            for i in mul:
                con += str(num*i)
        pros.append(pro)
        multis.append(multi)
    print pros
    print multis
    return max(pros[0])

print pandigitalMultiples()