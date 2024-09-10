# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Iterate every pair of nodes
        first, second = head, head.next
        while second:
            # Find the greatest common divisor
            divisor = gcd(first.val, second.val)

            # Insert it between
            node = ListNode(divisor)
            first.next = node
            node.next = second

            # And continue iterating list
            first, second = second, second.next

        # Return the modified linked list
        return head

# The runtime of the gcd algorithm is O(log(min(a, b))). As numbers
# here are constrained by 1 <= node.val <= 1000, we assume the additional
# complexity remains constant (log(1000) = 3).