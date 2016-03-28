def smallestMultiple(n):
    mul = 1
    divs = []
    for num in xrange(2, n+1):
        for div in divs:
            if num%div == 0:
                num = num/div
        if num != 1:
            divs.append(num)
            mul *= num
    return mul

print smallestMultiple(20)