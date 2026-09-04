class Solution:
    def trap(self, height: List[int]) -> int:
        # Me and Fiona's soln

        l = 0
        r = len(height)-1
        maxLeft = height[l]
        maxRight = height[r]
        water = 0

        while l <= r:
            if maxLeft <= maxRight:
                if maxLeft - height[l] > 0:
                    water += maxLeft - height[l]
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                if maxRight - height[r] > 0:
                    water += maxRight - height[r]
                maxRight = max(maxRight, height[r])
                r -= 1
        return water