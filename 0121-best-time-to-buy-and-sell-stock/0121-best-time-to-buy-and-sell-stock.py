class Solution(object):
    def maxProfit(self, prices):
        min_prices=float("inf")
        max_profit=0
        n=len(prices)

        for i in range(0,n):
            min_prices=min(min_prices, prices[i])
            max_profit=max(max_profit,prices[i]-min_prices)
        return max_profit
        
        