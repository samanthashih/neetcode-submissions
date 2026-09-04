class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Sorted increasing
        # 2 ptr: left=0, right=len(nums)
        # left -> inc if currSum < target (need more sum)
        # right -> dec if currSum > target (need less sum)

        left = 0
        right = len(numbers)-1

        while left < right:
            currSum = numbers[left]+numbers[right]
            if currSum < target:
                left += 1
            elif currSum > target:
                right -=1 
            else:
                return [left+1, right+1] # +1 bc 1-indexed array

        return [-1,-1]