class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window - maximize right-left profit
        # calc window profit (right-left)
        # if profit < maxProfit -> this was a bad day to buy -> left ++ 
            # if left == right, also inc right++
        # if proift >= maxProfit -> continue to see if there's a better sell day -> right++

        maxProfit = 0
        if len(prices) < 2:
            return maxProfit

        leftMostMin = prices[0]
        currDay = 0
        
        while currDay < len(prices):
            profit = prices[currDay] - leftMostMin
            print("profit: ", profit)

            leftMostMin = min(leftMostMin, prices[currDay])

            maxProfit = max(maxProfit, profit)
            currDay += 1
        
        return maxProfit
                
                