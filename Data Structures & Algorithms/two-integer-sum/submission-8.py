class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[j] = target - nums[i]
        # find nums[j] by indexing into hashmap containing all the {nums:[index, index, ..]}
            # If i == j -> check if nums[j] has another index for j

        numsIndex = defaultdict(list)

        for i in range(len(nums)):
            numsIndex[nums[i]].append(i)

        for i in range(len(nums)):
            numsJ = target - nums[i]

            if numsJ in numsIndex:
                for j in numsIndex[numsJ]:
                    if i != j:
                        return [i, j]
        
