def nonConstructibleChange(coins):
    sorted_coins = sorted(coins)
    change = 0

    for coin in sorted_coins:
        if coin > (change + 1):
            return change + 1
        else:
            change += coin

    return change + 1