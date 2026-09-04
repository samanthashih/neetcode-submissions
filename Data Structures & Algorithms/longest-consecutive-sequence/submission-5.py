class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert nums to set(nums) for O(1) lookup
        # For each num, try to find num+1 in set. Track maxChain
        numSet = set(nums)
        maxChain = 0

        for num in numSet:
            currCountNum = num
            currChain = 1
            while currCountNum+1 in numSet:
                currCountNum += 1
                currChain += 1
            # chain broken. Record maxChain
            maxChain = max(maxChain, currChain)
            # Reset
        return maxChain
            


        # # Iterate each num + try to build chain by checking if next num is +1 until chain breaks
        # # Store length chains={ startingNum 2 : length 1, 20:1, 4:1, 10:1, 3:3} -> rewrite w/ max val
        # # reset chain length

        # # Iterate thru chains{}. Store maxChain
        # # For 2:1, add maxChain += 1 -> try chains[2+1] and add if there chains[3]=3 so maxChain += 3

        # if len(nums) == 0:
        #     return 0
        # elif len(nums) == 1:
        #     return 1

        # chains = defaultdict(int)

        # i = 1
        # startingNum = nums[0]
        # currChain = 1
        # while i < len(nums):
        #     print("num: ", nums[i])
        #     print("startingNum: ", startingNum)
        #     if nums[i-1]+1 == nums[i]:
        #         currChain += 1
        #         print("inc chain")
        #     else:
        #         chains[startingNum] = max(chains[startingNum], currChain)
        #         startingNum = nums[i]
        #         currChain = 1
        #         print("restart chain")
        #     i += 1
        #     print("chains: ", chains)
        # chains[startingNum] = max(chains[startingNum], currChain)
        # print("chains: ", chains)

        # maxChain = 0
        # currBuildChain = 0
        # for startingNum in chains:
        #     while startingNum in chains:
        #         currBuildChain += chains[startingNum]
        #         startingNum += chains[startingNum]

        #     maxChain = max(maxChain, currBuildChain)
        #     currBuildChain = 0
        return maxChain
        
            
            