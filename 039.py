import math

def integerRightTriangles(num):
    count = 0
    for p in xrange(1, num+1):
        tris = []
        for a in xrange(1, p/3):
            for b in xrange(a+1, p/2):
                c = p - a - b
                if a*a + b*b == c*c:
                    tris.append((a, b, c))
        if len(tris) > count:
            count = len(tris)
            triMax = tris
            pMax = p
    print count, triMax
    return pMax

def integerRightTriangles2(num):
    count = 0
    for p in xrange(1, num+1):
        tris = []
        for a in xrange(1, int(p-p/math.sqrt(2))):
            b = p*(p-2*a)/2.0/(p-a)
            if b == int(b):
                tris.append((a, int(b), int(p-a-b)))
        if len(tris) > count:
            count = len(tris)
            triMax = tris
            pMax = p
    print count, triMax
    return pMax

print integerRightTriangles2(1000)