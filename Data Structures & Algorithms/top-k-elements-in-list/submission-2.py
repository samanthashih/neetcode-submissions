import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # max heap by count of (count, num)

        # hashmap {num:count}
        # convert to list [(num, count)] -> heapify_max(list)
        # pop top element k times

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        counts_list = [(-count, num) for num, count in counts.items()]
        # for num, count in counts.items():
        #     counts_list.append((num, count))

        # heapify implements minheap default
        # can do heapq.heapify_max(list), but heapify.heappop(list) will reheap it as min heap
        # to do a "max" with a minheap -> store values as negative
        heapq.heapify(counts_list)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(counts_list)[1])
        return ans



# test case 1
nums = [1,2,2,3,3,3]
k = 2
print(Solution().topKFrequent(nums, k)) # [2,3]
