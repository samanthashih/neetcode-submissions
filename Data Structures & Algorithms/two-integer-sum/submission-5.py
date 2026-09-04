class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2 pointer -> Inc L if need bigger sum / Dec R if need smaller sum
        # until find matching pair
        # Need to have sorted arr ^ but still want to keep track of og arr indices


        sorted_list = sorted(list(enumerate(nums)), key=lambda item: item[1]) # [(0,x), (1,x), (2,x)...]
        l = 0
        r = len(nums) - 1

        while (l < r):
            total = sorted_list[l][1] + sorted_list[r][1]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return sorted([sorted_list[l][0], sorted_list[r][0]])