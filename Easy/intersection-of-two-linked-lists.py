# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Iterate both linked lists at the same time
        currentA, currentB = headA, headB
        while currentA != currentB:
            # Whenever either list hits their end, begin iterating the other
            if not currentA:
                currentA = headB
            else:
                currentA = currentA.next

            if not currentB:
                currentB = headA
            else:
                currentB = currentB.next
            
        # And return their current value, either their intersection or their end
        return currentA


# This solution works as iterating A + B is the same as iterating B + A.
# Either, they are not intersecting, and both hit the end (None) at the same time.

# Or they are intersecting at a node at distance x from the end. This means that the
# intersecting node is at position A + B - x. This is also the same as B + A - x.
# Thus, each pointer will also hit this node at the same time.