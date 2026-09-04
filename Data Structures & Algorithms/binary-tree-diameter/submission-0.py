# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs
        # max left subtree depth, max right subtree depth

        res = 0
        
        def dfs(root):
            nonlocal res 
            
            if root == None:
                return 0
            
            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)
            res = max(res, leftDepth+rightDepth)

            return max(leftDepth, rightDepth) + 1
        
        dfs(root)
        return res