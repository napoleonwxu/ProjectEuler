'''#72s
def longestCollatzSequence(num):
    longest = 0
    longestNum = 0
    for i in xrange(1, num):
        print i
        n = i
        count = 1
        while n != 1:
            #print n
            if n%2 == 0:
                n = n/2
                count += 1
            else:
                n = 3*n+1
                count += 1
        if count > longest:
            longest = count
            longestNum = i
    return longestNum, longest
print longestCollatzSequence(1000000)
'''
def collatz(n):
    #if n not in colenth.keys():    #Very very very SLOW !!!
    if not colenth.get(n):  #36s
        if n%2 == 0:
            colenth[n] = collatz(n/2) + 1
        else:
            colenth[n] = collatz(n*3+1) + 1
    return  colenth[n]
colenth = {1:1}
longestNum = 1
longest = 1
for n in xrange(2, 1000000):
    print n
    if collatz(n) > longest:
        longestNum = n
        longest = colenth[n]
print longestNum, longest
