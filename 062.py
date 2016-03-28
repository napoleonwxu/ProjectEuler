def cubicPermutations(num):
    d = {}
    n = 1
    while True:
        c = n**3
        l = sorted(str(c))
        key = ''.join(l)
        if not d.get(key):
            d[key] = [1, c]
        else:
            d[key][0] += 1
            if d[key][0] == num:
                print key, n
                return d[key][1]
        n += 1

def cubicPermutations2(num):
    d = {}
    n = 1
    while True:
        c = n**3
        l = sorted(str(c))
        key = ''.join(l)
        if not d.get(key):
            d[key] = [n]
        else:
            d[key] += [n]
            if len(d[key]) == num:
                print d[key]
                return d[key][0] ** 3
        n += 1

print cubicPermutations2(5)