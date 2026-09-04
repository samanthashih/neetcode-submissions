# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
                # For each node in toVisit
        # Add children toVisit
        # swap left & right

        toVisit = deque()
        toVisit.append(root)

        while (len(toVisit) > 0):
            curr = toVisit.popleft()
            if (curr == None):
                break

            if (curr.left != None):
                toVisit.append(curr.left)
            if (curr.right != None):
                toVisit.append(curr.right)
            
            temp = curr.left
            curr.left = curr.right
            curr.right = temp

        return root