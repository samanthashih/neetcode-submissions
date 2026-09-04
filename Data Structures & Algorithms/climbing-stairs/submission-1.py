class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case
        if n == 1: return 1
        if n == 2: return 2
        
        numWays = [0]*(n+1)

        # last move could have taken 1step or 2steps to get to n
        #                       from step n-1   from step n-2
        # fibonacci

        # tabulation table -> store # ways to get to ith step
        # n = 1 -> 1 way
        numWays[1] = 1
        # n = 2 -> 2 ways
        numWays[2] = 2
        # n = 3 -> 2ways(from n=2) + 1step, 1 way(from n=1)+2step -> 3 ways
        # n = 4 -> 3 ways(from n=3) + 1step, 2ways + 2step -> 5 ways

        for i in range(3, n+1):
            # ways = 1step from [i-1] + 2steps from [i-2]
            numWays[i] = numWays[i-1] + numWays[i-2]

        return numWays[n]
                
