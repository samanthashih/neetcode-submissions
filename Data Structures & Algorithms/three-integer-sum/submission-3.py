class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] = -nums[k]

        # Convert numsIndex={ num : index }
        numsIndex = defaultdict(list)
        for i, num in enumerate(nums):
            numsIndex[num].append(i)

        # for each pair (i, j) search numsIndex[-k]
        # No dupes -> triplets ans is set()
        triplets = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                possibleKs = numsIndex[-(nums[i]+nums[j])]
                for k in possibleKs:
                    if i != k and j != k:
                        triple = [nums[i],nums[j],nums[k]]
                        triple.sort()
                        print("triple: ", triple)
                        if triple not in triplets:
                            triplets.append(triple)
        print("triplets: ", triplets)
        return triplets
