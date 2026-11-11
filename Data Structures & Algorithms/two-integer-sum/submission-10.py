class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsIndices = defaultdict(int)
        for i, n in enumerate(nums):
            if target-n in numsIndices and i != numsIndices[target-n]:
                return [numsIndices[target-n], i]
            numsIndices[n] = i

        return [-1, -1]