# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left, parent, right


        # stack -> add to stack
        # -> add parent to stack
        # -> add right to stack 

        stack = deque()
        visited = set()
        result = []

        stack.append(root)
        visited.add(root)
        while stack:
            curr = stack[-1]
            if curr == None:
                break
                
            while curr.left is not None and curr.left not in visited:
                stack.append(curr.left)
                visited.add(curr.left)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)

            if curr.right and curr.right not in visited:
                stack.append(curr.right)
                visited.add(curr.right)
        return result
        # stack = 7
        # result = 4,2,5,1,6,3
        # visited = 1,2,4,5,3
        # curr = 3



            
                
            

        
