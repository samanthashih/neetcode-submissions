# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if leftDepth vs rightDepth off by more than 1 -> balanced = False
        # depth of root = max(leftDepth, rightDepth) + 1

        balanced = [True]

        def maxDepth(root):
            if root == None:
                return 0
            
            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)

            if leftDepth < rightDepth and leftDepth+1 != rightDepth:
                balanced[0] = False
            elif leftDepth > rightDepth and leftDepth != rightDepth + 1:
                balanced[0] = False

            return max(leftDepth, rightDepth) + 1

        maxDepth(root)
        return balanced[0]