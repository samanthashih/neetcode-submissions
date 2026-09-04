# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Each node. swap children left right
        # Add children nodes toVisit

        toVisit = deque()
        if root == None:
            return None

        curr = root
        toVisit.append(curr)

        while toVisit:
            curr = toVisit.popleft()

            temp = curr.left
            curr.left = curr.right
            curr.right = temp

            if curr.left:
                toVisit.append(curr.left)
            if curr.right:
                toVisit.append(curr.right)
        
        return root
            