# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using two pointer

        # First, iterate to the middle element
        fast, slow, last = head, head, None
        while fast and fast.next:
            # Iterate fast pointer twice the speed of slow
            fast = fast.next.next

            # Iterate slow pointer once, storing last seen element as well
            last = slow
            slow = slow.next
        
        # Delete the middle element
        if last is not None:
            last.next = slow.next
        else:
            head = None
        
        # And return the new linked list
        return head
