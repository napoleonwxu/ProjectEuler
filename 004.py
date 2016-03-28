def maxPalindrome_6digit():
    half = 999
    while half >= 100:
        palindrome = half*1000 + (half%10)*100 + (half/10%10)*10 + half/100
        factor = 999
        while factor >= 100:
            if palindrome%factor == 0 and palindrome/factor <= 999:
                print palindrome, '=', factor, '*', palindrome/factor
                return palindrome
            factor -= 1
        half -= 1

maxPalindrome_6digit()