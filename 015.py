def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

def latticePaths(n, m): # C(n+m, n)
    return fact(n+m) / fact(n) / fact(m)

print latticePaths(20, 20)