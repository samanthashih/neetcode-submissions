class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,3,12,1,2]
        # buy = 1
        # sell = 2
        # maxProfit = 9

        # Sliding window: left/buy + right/sell ptr
        # Increase window (right++)

        # when we hit a new minimum buy price + check max(profit, maxProfit)
        # -> then move left to new minimum buy

        # Keep track of maxProfit

        buy = 0
        sell = 0
        maxProf = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            print("new profit ", profit)
            maxProf = max(maxProf, profit)
            if prices[sell] < prices[buy]:
                buy = sell
                print("new buy price ", buy)
            print("new sell price ", sell)
            sell += 1
        return maxProf

        # [10,3,12,1,2]
        # buy = 1
        # sell = 2
        # maxProfit = 9

        # [7,1,5,3,6,4]
        # buy = 1
        # sell = 4
        # maxProfit = 5
        