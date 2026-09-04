class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort & iterate thru sorted to find longest chain -> O(logn+n)

        # convert nums to dict for O(1) lookup -> O(n)
        # iterate nums to create chains by looking for num+1 in dict
            # only check for numbers that are starting values (num-1 does not exist)
        
        numsSet = set(nums)
        maxLength = 0

        for num in nums:
            if num-1 not in numsSet:
                # we know num is a starting chain
                nextNum = num+1
                length = 1
                while nextNum in numsSet: # create & count chain
                    length += 1
                    nextNum += 1
                maxLength = max(maxLength, length)

        return maxLength
                