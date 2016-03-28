def isLychrel(n):
    t = n + int(''.join(reversed(str(n))))
    for i in xrange(50):
        p = int(''.join(reversed(str(t))))
        if p == t:
            return False
        else:
            t += p
    return True

def lychrelNumbers(num):
    count = 0
    for n in xrange(num):
        if isLychrel(n):
            count += 1
    return count

#print isLychrel(349)
print lychrelNumbers(10000)