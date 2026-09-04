# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter of root = maxHeight(leftTree) + maxHeight(rightTree)
        # maxHeight = max( maxheight(leftTree), maxheight(rightTree) ) + 1

        maxDiameter = [0]

        def maxDepth(root):    
            if root == None:
                return 0 # height of 0

            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)

            maxDiameter[0] = max(maxDiameter[0], leftDepth + rightDepth)

            return max(leftDepth, rightDepth) + 1
            
        maxDepth(root)
        return maxDiameter[0]