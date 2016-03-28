def numberLetterCounts1000():
    letterCounts1000 = [0] * 1001
    for i in (1, 2, 6, 10):
        letterCounts1000[i] = 3
    for i in (3, 7, 8, 40, 50, 60):
        letterCounts1000[i] = 5
    for i in (4, 5, 9):
        letterCounts1000[i] = 4
    for i in (11, 12, 20, 30, 80, 90):
        letterCounts1000[i] = 6
    for i in (13, 14, 18, 19):
        letterCounts1000[i] = 8
    for i in (15, 16, 70):
        letterCounts1000[i] = 7
    letterCounts1000[17] = 9
    for i in xrange(20, 100, 10):
        for j in xrange(1, 10):
            letterCounts1000[i+j] = letterCounts1000[i] + letterCounts1000[j]
    for i in xrange(100, 1000, 100):
        letterCounts1000[i] = letterCounts1000[i/100] + len('hundred')
    for i in xrange(100, 1000, 100):
        for j in xrange(1, 100):
            letterCounts1000[i+j] = letterCounts1000[i] + len('and') + letterCounts1000[j]
    letterCounts1000[1000] = len('one') + len('thousand')

    return sum(letterCounts1000)

print numberLetterCounts1000()