class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Find minLeft to buy, maxRight to sell
        # l = 0 -> if we find a val < l, move l
        # r = 0 -> profit = r-l. max(maxProfit, profit). r++

        l = 0
        r = 0
        maxProfit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            maxProfit = max(maxProfit, prices[r]-prices[l])
            r += 1
        
        return maxProfit