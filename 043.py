def generateNum(nums):
    if len(nums) == 1:
        yield str(nums[0])
    for i in xrange(len(nums)):
        for s in generateNum(nums[:i]+nums[i+1:]):
            yield str(nums[i]) + s

def subStringDivisibility():    # slow
    res = []
    nums = [i for i in xrange(10)]
    primes = [2, 3, 5, 7, 11, 13, 17]
    for s in generateNum(nums):
        #print s
        flag = True
        if s[0] == '0':
            continue
        if int(s[3]) not in [0, 2, 4, 6, 8]:
            continue
        if int(s[5]) not in [0, 5]:
            continue
        print s
        for i in xrange(len(primes)):
            if int(s[i+1:i+4]) % primes[i] != 0:
                flag = False
                break
        if flag == True:
            res.append(int(s))
    print res
    return sum(res)

def property(numStr, products):
    if len(numStr) == 0:
        for d in products[0]:
            for sub in property(d, products):
                for i in xrange(10):
                    if str(i) not in d+sub:
                        yield int(str(i) + d + sub)
    else:
        for d in products[len(numStr)-2]:
            if d[:2] == numStr[-2:] and d[2] not in numStr:
                if len(numStr) == 8:
                    yield d[2]
                else:
                    for sub in property(numStr+d[2], products):
                        yield d[2] + sub

def subStringDivisibility2():   # fast
    res = []
    products = []
    primes = [2, 3, 5, 7, 11, 13, 17]
    for prime in primes:
        pros = []
        i = 1
        pro = prime * i
        while pro < 1000:
            a, b , c = pro/100, (pro/10)%10, pro%10
            if a !=b and a != c and b != c:
                if pro < 100:
                    pros.append('0'+str(pro))
                else:
                    pros.append(str(pro))
            i += 1
            pro = prime * i
        products.append(pros)
    #print products
    for num in property('', products):
        res.append(num)
    print res
    return sum(res)

print subStringDivisibility2()
