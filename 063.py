import math

def powerfulDigitCounts(nMax):
    count = 0
    for n in xrange(1, nMax+1):
        i = 1
        length = len(str(i**n))
        while length <= n:
            if length == n:
                count += 1
            i += 1
            length = len(str(i**n))
    return count

#print powerfulDigitCounts(21)

counter = 0
for n in range(1, 22):
    counter += 10-int(math.ceil(10**((n-1)/float(n))))
print counter