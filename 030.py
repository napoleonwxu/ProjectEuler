def digitFifthPowers(num):
    fifthPowers = []
    for n in xrange(2, num):
        sumPowers  = 0
        temp = n
        while temp > 0:
            sumPowers += (temp%10)**5
            temp /= 10
        if n == sumPowers:
            fifthPowers.append(n)
    print fifthPowers
    return sum(fifthPowers)

print digitFifthPowers(10**6)
