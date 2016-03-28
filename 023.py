def isAbundant(num):
    sum = 1
    i = 2
    while i*i < num:
        if num%i == 0:
            sum += i
            sum += num/i
        i += 1
    if i*i == num:
        sum += i
    if sum > num:
        return True
    else:
        return False

def nonAbundantSums():
    abundantNums = []
    for n in xrange(2, 28123+1):
        if isAbundant(n) == True:
            abundantNums.append(n)
    #print abundantNums
    l = len(abundantNums)
    #print l
    isAbundantSum = [False] * (28123+1)
    for i in xrange(l):
        for j in xrange(i, l):
            s = abundantNums[i] + abundantNums[j]
            if s <= 28123:
                isAbundantSum[s] = True

    sum = 0
    for i in xrange(1, 28123+1):
        if isAbundantSum[i] == False:
            #print i
            sum += i
    return sum

print nonAbundantSums()