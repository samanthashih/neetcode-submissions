class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 ptr -> want tall bars + far apart
        # left, right -> move smaller ptr inwards (want to keep bigger ptr to maximize)

        # area = w*h = (bar2-bar1) * min(bar1, bar2)


        left = 0
        right = len(heights)-1
        maxArea = 0
        
        while left < right:
            area = (right-left) * min(heights[left], heights[right])
            maxArea = max(maxArea, area)

            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1                
        return maxArea
        