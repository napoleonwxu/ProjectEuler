def generateDigitals(digits):
    if len(digits) == 1:
        yield digits
    for i in xrange(len(digits)):
        digitsRest = digits[:i] + digits[i+1:]
        for digitsAdd in generateDigitals(digitsRest):
            yield [digits[i]] + digitsAdd

def pandigitalProductsSum():
    multiplicand = []
    multiplier = []
    products = []
    for d in generateDigitals([1, 2, 3, 4, 5, 6, 7, 8, 9]):
        product = 1000*d[5]+100*d[6]+10*d[7]+d[8]
        if d[0] * (1000*d[1]+100*d[2]+10*d[3]+d[4]) == product:
            products.append(product)
            multiplicand.append(d[0])
            multiplier.append(1000*d[1]+100*d[2]+10*d[3]+d[4])
        if (10*d[0]+d[1]) * (100*d[2]+10*d[3]+d[4]) == product:
            products.append(product)
            multiplicand.append(10*d[0]+d[1])
            multiplier.append(100*d[2]+10*d[3]+d[4])
    print multiplicand
    print multiplier
    print products
    return sum(set(products))

print pandigitalProductsSum()