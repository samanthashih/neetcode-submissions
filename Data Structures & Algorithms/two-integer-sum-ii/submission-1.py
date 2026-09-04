class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1-indexed array -> +1 to answers

        # 2 ptr
            # left++ if sum < target
            # right-- if sum > target 
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return [left+1, right+1]
        
        # no valid answer
        return [-1, -1]

# test case 1
numbers = [1,2,3,4]
target = 3
print(Solution().twoSum(numbers, target)) # [1,2]