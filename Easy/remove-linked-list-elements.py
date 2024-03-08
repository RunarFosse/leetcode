# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # If we are at the end, stop
        if not head:
            return head

        # If we should remove current, return pointer to next node
        if head.val == val:
            return self.removeElements(head.next, val)
        
        # If not, keep head and recurse
        head.next = self.removeElements(head.next, val)
        return head