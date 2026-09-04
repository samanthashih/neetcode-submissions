class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6] to exclude 4 = 1*2* 4 *6 / 4 

        # without division
        # need the prefix product 1*2 and the suffix product *6
        # calc each num prefix product -> store in list
            # same for suffix product -> store in list
        # ans[i] = prefix[i]*suffix[i]

        prefix = []
        currProduct = 1
        for num in nums:
            prefix.append(currProduct)
            currProduct *= num

        suffix = []
        currProduct = 1
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            suffix.append(currProduct)
            currProduct *= num
        
        print("prefix: ", prefix)
        print("suffix: ", suffix)

        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[len(nums)-1-i])
        return ans