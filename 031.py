def coinSums(money, coinList):
    count = 0
    for i in xrange(len(coinList)):
        moneyLeft = money - coinList[i]
        if moneyLeft == 0:
            count += 1
        elif moneyLeft > 0:
            count += coinSums(moneyLeft, coinList[:i+1])
    return count

print coinSums(200, [1, 2, 5, 10, 20, 50, 100, 200])