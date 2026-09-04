import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get top elements -> heapq !

        # nums_count = {num:count}
        # heapify nums_count by value/count -> heapify(list) is minheap default so to maxheap, use negative values
                # heapq.heapify(list) -> heapify in place, don't store in new var
            # need to create nums_count list[(count, num), (count, ...)] -> heapify based on 1st tuple element
        # get top K from heap
            # heapq.heappop(list) * k times

        nums_count = defaultdict(int)
        for n in nums:
            nums_count[n] += 1
        
        nums_count_heap = []
        for key, val in nums_count.items():
            nums_count_heap.append((-val, key))
        heapq.heapify(nums_count_heap)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(nums_count_heap)[1])
        return ans