# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs on pRoot qRoot
        # If pRoot.val != qRoot.val -> equivalent = false

        equivalent = [True]

        def dfs(pRoot, qRoot):
            if pRoot == None and qRoot == None:
                return
            elif pRoot == None and qRoot != None:
                equivalent[0] = False
                return
            elif pRoot != None and qRoot == None:
                equivalent[0] = False
                return 
            
            if pRoot.val != qRoot.val:
                equivalent[0] = False

            dfs(pRoot.left, qRoot.left)
            dfs(pRoot.right, qRoot.right)

            return
        
        dfs(p, q)
        return equivalent[0]