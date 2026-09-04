class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        # Neetcode vid: 2 ptr
        # left = 0, right = len(height)
        # Track maxLeft, maxRight. 
        # For each left, calc water we can store @ left
            # water = min(maxLeft, maxRight) - h[left]
        # Update maxLeft, maxRight
        # If maxLeft <= maxRight -> left++. Else -> right--

        l = 0
        r = len(height)-1
        maxLeft = height[l]
        maxRight = height[r]
        water = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]
                
        return water



        