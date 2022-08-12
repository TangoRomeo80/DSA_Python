def maxProfit(prices):
    l, r = 0, 1 #left=buy, right=sell
    max_profit = 0
    while r < len(prices):
        #profitable?
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
        else:
            l = r
        r += 1

    return max_profit
