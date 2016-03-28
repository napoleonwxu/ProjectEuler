import math

def test(p, index):
    if index == 3:
        n = (math.sqrt(8*p+1)-1)/2
    elif index == 4:
        n = math.sqrt(p)
    elif index == 5:
        n = (math.sqrt(24*p+1)+1)/6
    elif index == 6:
        n = (math.sqrt(8*p+1)+1)/4
    elif index == 7:
        n = (math.sqrt(40*p+9)+3)/10
    if n == int(n):
        return True

def figure(p, res, index):
    res[index-3] = p
    if res.count(0) == 0 and p%100 == res[5]/100:
        print res, sum(res)
    for p_ in xrange(10, 100):
        pp = (p%100)*100 + p_
        for i in xrange(7, 2, -1):
            if res[i-3] == 0 and test(pp, i):
                figure(pp, res, i)
                res[i-3] = 0

def cyclicalFigurateNumbers():
    for n8 in xrange(19, 59):  #19*(3*19-2)=1045; 58*(3*58-2)=9976
        p8 = n8*(3*n8-2)
        if p8%100 >= 10:
            res = [0, 0, 0, 0, 0, 0]
            figure(p8, res, 8)

cyclicalFigurateNumbers()