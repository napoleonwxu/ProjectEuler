def hasNDistinctPrimesFactors(num, N):
    factors = []
    if num%2 == 0:
        factors.append(2)
        while num%2 == 0:
            num /= 2
    i = 3
    while num > 1:
        if num%i == 0:
            factors.append(i)
            while num%i == 0:
                num /= i
        i += 2
    if len(factors) == N:
        return True
    return False

def nConsecutiveIntegers(N):
    n = 2
    while True:
        flag = 0
        while flag < N:
            if hasNDistinctPrimesFactors(n, N):
                flag += 1
                n += 1
            else:
                n += 1
                break
        print n
        if flag == N:
            return n-N

print nConsecutiveIntegers(4)
#print hasNDistinctPrimesFactors(647)
