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

        def maxHeight(root):    
            if root == None:
                return 0 # height of 0

            leftHeight = maxHeight(root.left)
            rightHeight = maxHeight(root.right)

            maxDiameter[0] = max(maxDiameter[0], leftHeight + rightHeight)

            return max(leftHeight, rightHeight) + 1
            
        maxHeight(root)
        return maxDiameter[0]