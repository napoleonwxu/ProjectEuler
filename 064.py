import math

#http://www.kylen314.com/archives/4943
def getPeriodSquareRoots(s):
    m = 0
    d = 1
    a0 = int(math.sqrt(s))
    a = a0
    length = 0
    while a != 2*a0:
        m = a*d - m
        d = (s-m*m)/d
        a = int((math.sqrt(s)+m)/d)
        length += 1
    return length

def oddPeriodSquareRoots(num):
    count = 0
    for s in xrange(2, num+1):
        if int(math.sqrt(s)) != math.sqrt(s):
            if getPeriodSquareRoots(s)%2 == 1:
                count += 1
    return count

print oddPeriodSquareRoots(10000)