class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force
        # iterating thru nums, make tracking list of seenNumbers, check num in seenNumbers -> return True if we hit dupe

        # improvement
        # hashmap seenNumbers for O(1) access to check

        seenNumbers = {}
        for n in nums:
            if n not in seenNumbers: # we found an unseen number
                seenNumbers[n] = True
            else: # we found a dupe -> return True
                return True
        
        # we made it thru all of nums without finding dupe -> return False
        return False

# test case
nums = [1, 2, 3, 3]
print("test1: ", Solution().hasDuplicate(nums)) # True
