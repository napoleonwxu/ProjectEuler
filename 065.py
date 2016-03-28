def convergentsOfE(n):
    if n == 1:
        return 2
    if n%3 == 0:
        nu, de = 1, 2*(n/3)
    else:
        nu, de = 1, 1

    n -= 1
    while n > 1:
        if n%3 == 0:
            nu, de = de, 2*(n/3)*de+nu
        else:
            nu, de = de, de+nu
        n -= 1
    nu = 2*de+nu
    print nu, de

    res = 0
    for i in str(nu):
        res += int(i)
    return res

print convergentsOfE(100)

