def isPalindrome(n):
    if n%10 == 0:
        return False
    temp = 0
    while n > temp:
        temp = 10*temp + n%10
        n /= 10
    if n == temp or n == temp/10:
        return True
    return False

def isBinPalindrome(n):
    nBinStr = str(bin(n))
    nBin = int(nBinStr[2:])
    return isPalindrome(nBin)

def doubleBasePalindromes(num):
    doublePalindromes = []
    for n in xrange(1, num, 2): #odd only
        if isPalindrome(n) and isBinPalindrome(n):
            doublePalindromes.append(n)
    print len(doublePalindromes)
    print doublePalindromes
    return sum(doublePalindromes)

print doubleBasePalindromes(10**6)