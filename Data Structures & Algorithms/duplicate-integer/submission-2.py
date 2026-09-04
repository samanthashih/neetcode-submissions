class Solution: # 1/6/26
    def hasDuplicate(self, nums: List[int]) -> bool:
        # keep track of seen nums
        # for each n in nums:
            # check if n is seen -> return True (dupe found)
        

        seenNums = {}

        for n in nums:
            if n not in seenNums:
                seenNums[n] = True
            else:
                return True
        
        return False

# test case
res1 = Solution().hasDuplicate([1, 2, 3, 3]) # true
print(res1) 

res2 = Solution().hasDuplicate([1, 2, 3, 4]) # false
print(res2) 