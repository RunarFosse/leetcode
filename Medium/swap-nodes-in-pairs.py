# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If end of list you can't swap
        if not head or not head.next:
            return head

        # Swap and return new head
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head

        return second
