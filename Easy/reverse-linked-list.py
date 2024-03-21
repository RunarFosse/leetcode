# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Reverse each link in list
        last = None
        while head:
            # Temporarily store next node
            temp = head.next

            # Flip the link
            head.next, last = last, head
  
            # Continue
            head = temp
        
        # As head now is None, return the last node
        return last