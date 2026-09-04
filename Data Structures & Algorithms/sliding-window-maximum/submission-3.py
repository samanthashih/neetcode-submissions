import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force. Slide window l++, r++ and compare all k (ex. 3) nums O(k*n)
        # optimize: get window's max O(1) -> maxheap

        res = []
        l = 0
        r = k - 1

        # initialize heap. store indexes (val, index)
        maxHeap = []
        for i in range(l, r+1):
            maxHeap.append((nums[i], i))
        heapq.heapify_max(maxHeap)

        while r < len(nums):
            # print("maxHeap: ", maxHeap)

            # Add curr window's max to res
            res.append(maxHeap[0])

            # Slide window and update heap (first check index r for Out of Bounds)
            # if max moves out of window (max's index < l) -> keep heappopping until heaps' max is in window
            l += 1
            r += 1
            if r < len(nums):
                heapq.heappush_max(maxHeap, (nums[r], r))
            while maxHeap != [] and maxHeap[0][1] < l:
                heapq.heappop_max(maxHeap)
            
        return [item[0] for item in res]