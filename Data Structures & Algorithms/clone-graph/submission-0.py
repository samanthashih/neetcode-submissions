"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        storeReferences = {}

        def recur(orig) -> Optional['Node']:
            newNode = Node(orig.val, [])
            storeReferences[orig] = newNode

            for origNeigh in orig.neighbors:
                if origNeigh not in storeReferences:
                    newNode.neighbors.append(recur(origNeigh))
                else:
                    newNode.neighbors.append(storeReferences[origNeigh])

            return newNode

        if node is None:
            return None
            
        return recur(node)
                

    
        