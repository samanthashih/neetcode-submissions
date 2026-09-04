class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (right + left) // 2
            if target > nums[mid]:
                # shift left ptr to mid
                left = mid + 1
            elif target < nums[mid]:
                # shift right ptr to mid
                right = mid - 1
            else:
                return mid

        return -1
