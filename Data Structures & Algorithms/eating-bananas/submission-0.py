class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        l = 1 # each pile guaranteed bananas, so min speed is 1. If l=0, we need to account for speed could be 0 then p/0 math err
        r = max(piles)
        res = r

        while (l <= r):
            hoursLeft = h
            speed = (l+r)//2 # Try speed

            for p in piles:
                hoursLeft -= math.ceil(p/speed)
                if hoursLeft < 0: # Ran out of time. Need bigger speed
                    l = speed + 1
                    break

            if hoursLeft >= 0: # Finished all piles in time. Speed worked, try for smaller speed
                res = min(res, speed)
                r = speed - 1
        return res


# # binary search
# l = 0
# r = len(arr) - 1
# while l <= r:
#     mid = (l+r)//2
#     if num > arr[mid]:
#         l = mid+1
#     elif num < arr[mid]:
#         r = mid-1
#     else:
#         return mid
# return -1