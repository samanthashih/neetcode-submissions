# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # k ptrs, one for each list
        # compare all k and append smallest. remove() None ptrs (when we reach end of a list)

        dummyHead = ListNode()
        dummyTail = dummyHead

        ptrs = []
        for head in lists:
            if head is not None:
                ptrs.append(head)
            
        # print("ptrs: ", ptrs)
        
        while ptrs:
            smallestPtr = ptrs[0]
            smallestPtrIndex = 0
            for i, ptr in enumerate(ptrs):
                if ptr.val < smallestPtr.val:
                    smallestPtr = ptr
                    smallestPtrIndex = i
            
            # res append smallestPtr
            dummyTail.next = smallestPtr
            dummyTail = dummyTail.next
            # move ptr down & del ptr if finished with list (ptr goes to None)
            if smallestPtr.next is None:
                del ptrs[smallestPtrIndex]
            else:
                ptrs[smallestPtrIndex] = smallestPtr.next
            
        dummyTail.next = None
        return dummyHead.next