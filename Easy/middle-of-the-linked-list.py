# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using fast/slow pointer
        slow, fast = head, head

        # While fast can move 2 steps
        while fast and fast.next:
            # Do so
            fast = fast.next.next

            # And move slow 1
            slow = slow.next
        
        # Return the slow node (this is the middle)
        return slow