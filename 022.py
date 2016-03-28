def editFile(fileName):
    f = open(fileName)
    for line in f:
        names = line.strip('"').split('","')
    names.sort()
    return names

def namesScores(names):
    scores = 0
    for i in xrange(len(names)):
        worth = 0
        for char in names[i]:
            worth += ord(char) - ord('A') + 1
        scores += worth * (i+1)
    return scores

fileName = 'p022_names.txt'
names = editFile(fileName)
print namesScores(names)