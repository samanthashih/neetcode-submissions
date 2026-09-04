class Solution:
    def trap(self, height: List[int]) -> int:
        # Esther's soln
        l,r = 0, len(height)-1
        area, minHeight = 0, 0

        while l < r:
            if height[l] <= height[r]:
                minHeight = height[l]
                while height[l] <= minHeight and l < r:
                    curr = minHeight - height[l]
                    area += curr if curr > 0 else 0
                    l += 1
            else:
                minHeight = height[r]
                while height[r] <= minHeight and l < r:
                    curr = minHeight - height[r]
                    area += curr if curr > 0 else 0
                    r -= 1
        return area