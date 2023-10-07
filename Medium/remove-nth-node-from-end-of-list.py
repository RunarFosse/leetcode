# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        # Keep track of node n positions behind current
        last, n_behind, curr = None, head, head
        depth = 0
        while curr:
            if depth == n:
                last = n_behind
                n_behind = n_behind.next
                depth -= 1
            depth += 1
            curr = curr.next

        # If we are removing the first, we return the second element
        if not last:
            return n_behind.next

        last.next = n_behind.next
        return head
        