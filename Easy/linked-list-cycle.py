# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using two pointer approach
        slow, fast = head, head
        while True:
            # Check if fast reached the end
            if not fast or not fast.next:
                return False

            # If not, increment them both and check if they overlap
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
# We use the two pointer approach, where we have a slow and a fast pointer.
# The slow pointer increments by one node every iteration whilst the fast pointer
# increments by two. If they ever meet, the linked list has a cycle. If not 
# (i.e. the fast pointer reaches the end), then it does not.