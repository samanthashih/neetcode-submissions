class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False


# test1 = [1, 5, 40, -3, 1, 4, 2]
# print(Solution().hasDuplicate(test1))