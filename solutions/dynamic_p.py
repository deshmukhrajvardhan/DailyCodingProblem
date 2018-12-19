def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    """
     coinValueList = [1,5,10,21,25] # list of possible coins
     change = 63 # Actual amount
     minCoins = [0,0...0] (64)
     coinsUsed = [0,0...0] (64)
    """
    count=0
    for cents in range(change + 1):  # loop 64 times
        coinCount = cents  # cents = 0,1..64 (iterations-wise)
        newCoin = min(coinValueList)
        # print("Cents:{}".format(cents))
        for j in [c for c in coinValueList if c <= cents]:  # list of usable coins in each iteration
            # print("j:{},minCoins:{};coinsUsed:{}".format(j, minCoins, coinsUsed))
            count+=1
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    print("dynamic_p number of iterations:{}".format(count))
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print("In printCoins:coin:{}".format(thisCoin))
        coin = coin - thisCoin


def main():
    amnt = 26
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)

    print("Making change for", amnt, "requires")
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)


main()