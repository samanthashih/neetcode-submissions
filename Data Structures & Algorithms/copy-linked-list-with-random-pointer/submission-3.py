"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # problem: random can point to future node (not created yet)
        # one pass: iterate og and create new nodes w/o setting random
        # two pass: iterate og and for each set new_node.random = new_node
            # need to maintain ptrs to all copy_nodes -> ogToNew = {og : new node version}
        
        # ogToNew = defaultdict(lambda: None)
        ogToNew = {}
        # one pass
        dummyHeadNew = Node(0)

        curr = head
        currNew = dummyHeadNew

        while curr:
            newNode = Node(curr.val)

            currNew.next = newNode
            ogToNew[curr] = newNode

            curr = curr.next
            currNew = currNew.next

        # two pass
        curr = head
        currNew = dummyHeadNew.next

        while curr:
            if curr.random is None:
                currNew.random
            else:
                currNew.random = ogToNew[curr.random]
            curr = curr.next
            currNew = currNew.next

        # return ptr of 1st real node
        return dummyHeadNew.next