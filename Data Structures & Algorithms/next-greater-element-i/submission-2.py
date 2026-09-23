class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = defaultdict()
        nums2_map = defaultdict()
        ans = []

        for i, n in enumerate(nums1):
            nums1_map[n] = i
        for i, n in enumerate(nums2):
            nums2_map[n] = i
        
        
        for i in range(0, len(nums1)):
            n1 = nums1[i]
            if n1 not in nums2_map:
                continue
            j = nums2_map[n1]

            while j < len(nums2):
                if nums2[j] > n1:
                    ans.append(nums2[j])
                    break
                j += 1
                
            if j == len(nums2):
                ans.append(-1)

        return ans