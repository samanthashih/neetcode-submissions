class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sort nums. Iterate thru and count each num
        # Make new list w/ counts [[num, count], [num,count], ...] from nums
        # Sort by count lambda item:item[1]
        # return top k from sorted

        nums = sorted(nums)
        counts = []

        counts_i = 0
        counts.append([nums[0],0])
        for n in nums:
            if n != counts[counts_i][0]:
                counts.append([n, 0])
                counts_i += 1
            counts[counts_i][1] += 1

        counts = sorted(counts, key=lambda item:item[1], reverse=True)

        res = []
        for i in range(k): 
            res.append(counts[i][0])
        return res