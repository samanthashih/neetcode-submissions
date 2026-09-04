class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search -> start middle, move to left middle if target smaller. move to right middle if target bigger

        l = 0
        r = len(nums)-1


        while l <= r:
            mid = (l+r) // 2
            print("mid: ", mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1