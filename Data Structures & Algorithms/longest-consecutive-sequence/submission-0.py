class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict_nums = {}
        for num in nums:
            dict_nums[num] = True
        
        maxChain = 0
        for num in nums:
            # check if num is start of a chain -> (num-1) will not exist in dict
            if ((num-1) not in dict_nums):
            # if yes, start counting up to create chain & keep track of maxLength
                currChain = 1
                nextNum = num+1

                while (nextNum in dict_nums):
                    currChain += 1
                    nextNum += 1

                maxChain = max(maxChain, currChain)
            # if no, skip num. eventually we will hit the number that is the start of num's chain
        
        
        return maxChain