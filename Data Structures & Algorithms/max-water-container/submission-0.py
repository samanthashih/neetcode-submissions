class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force -> iterate thru all pairs (possible buckets) O(n^2)

        # sliding window -> l = 0, r = len(heights)-1 -> this will maximize width
            # move smaller height pointer inwards
            # stop when l >= r
        
        l = 0
        r = len(heights)-1
        maxArea = 0

        while l < r:
            print("l: ", heights[l], " r: ", heights[r])
            area = min(heights[l], heights[r]) * (r-l) # height * width
            # print("area = ", min(heights[l], heights[r]), " * ", (r-l))
            maxArea = max(maxArea, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea
    
    