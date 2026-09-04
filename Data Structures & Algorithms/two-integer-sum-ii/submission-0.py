class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer: front + back
        # nums[front] + nums[back] > target: back-- (decrease total)
        # nums[front] + nums[back] < target: front++ (increase total)

        front = 0
        back = len(numbers) - 1

        while front < back:
            total = numbers[front] + numbers[back]
            if total > target:
                back -= 1
            elif total < target:
                front += 1
            else:
                return [front+1, back+1]

        # reminder: +1 to final indices bc 1-indexed
        