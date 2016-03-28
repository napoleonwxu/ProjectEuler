def maximumPathSum(tringle):
    i = len(tringle) - 2
    while i >= 0:
        for j in xrange(len(tringle[i])):
            tringle[i][j] += max(tringle[i+1][j], tringle[i+1][j+1])
        i -= 1
    return tringle[0][0]

def toInt(text):
    tringle = []
    for line in open(text, 'r'):
        tringle.append(line.split())
    for i in xrange(len(tringle)):
        for j in xrange(len(tringle[i])):
            tringle[i][j] = int(tringle[i][j])
    return tringle

textName = 'p067_triangle.txt'
print maximumPathSum(toInt(textName))