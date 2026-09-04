class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding window of buy/sell dates
        # buy = 0 -> if right<left price, we found a better buy price -> move left to = right. 
        # sell = 0 -> inc each time aka new day progressed
        # profit = prices[sell] - prices[buy]

        buy = 0
        sell = 0
        maxProfit = 0

        while sell < len(prices):
            profit = prices[sell]-prices[buy]
            maxProfit = max(maxProfit, profit)
            if profit < 0: # negative profit -> sell date is better to buy
                buy = sell
            sell += 1
        return maxProfit