class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Return true if nums has duplicates
        # Loop nums & keep track of seen nums -> {num: true/false}
        # -> if we find a seen num, return true immediately
        # -> if we reach end of array, return false

        seen_nums = {}

        for num in nums:
            if num in seen_nums:
                return True
            else:
                seen_nums[num] = True 
        
        return False
        
        # Test case
        # nums=[1,2,3,3]

        # seen_nums = {
            # 1: true,
            # 2: true,
            # 3: true
        # }
