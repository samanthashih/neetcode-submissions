class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def testRate(rate: int) -> bool:
            hoursUsed = 0

            # while bananas
            for p in piles:
                hoursUsed += math.ceil(p / rate)

                # if we're out of time, return false
                if (hoursUsed > h): return False
            return True

        # binary search all possible rates -> [1 ... max(piles)]
        # test each rate and keep track of working minRate

        # need at least len(piles) hours
        if len(piles) > h:
            return -1

        
        minRate = max(piles)

        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            works = testRate(mid)
            print("mid rate: ", mid, " works: ", works)
            if works:
                minRate = min(minRate, mid)
                right = mid-1
            else:
                left = mid+1
        return minRate
    

        

# piles = [1,4,3,2], h = 9

