class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # division solution: multiple all numbers together 1*2*3*4 = 24
            # divide 24 / nums[i] so it owuld cancel out 
            # like 1*2*3*4 / 2 -> 1*3*4-> put into sol[1]
            # PROBLEM: dividing by 0 :( or if there is a 0, the whole product is 0. 
                # we would need to find the product w/o 0 for when product*0 / 0 -> can't rly do this
        
        # [1,2,4,6]
        # 1 ->   * 2*4*6 
        # 2 -> 1 * 4*6
        # 4 -> 1*2 * 6 
        # 6 -> 1*2*4 * 
        # rightProduct -> starts w/ 6, keep multipling until 1st element
        # leftProduct -> starts w/ 1, keep multipling until last element
        # store each index's leftP, rightP -> res = leftP*rightP

        products = [] #[ [leftP,rightP], ...]

        leftProduct = 1
        for i in range(len(nums)): 
            products.append([leftProduct])
            leftProduct *= nums[i]

        rightProduct = 1
        for i in range(len(nums)-1, -1, -1): 
            products[i].append(rightProduct)
            rightProduct *= nums[i]
        # OPTIMIZE: don't need to store rightProduct bc we will immediately use & calc final answer
        # directly calc final res & return -> O(n) additional space (res array) 

        print(products)
        res = []
        for leftP, rightP in products:
            res.append(leftP*rightP)
        return res

# test 1
Solution().productExceptSelf([1,2,4,6])

