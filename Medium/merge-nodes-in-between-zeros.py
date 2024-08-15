# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use two pointers, one for iterating the list, one for inserting
        iterator = inserter = head

        # Keep track of current sum between zeros
        current = 0

        # And iterate list until termination,
        while iterator.next is not None:
            # Add current value to running sum and move iterator pointer
            iterator = iterator.next
            current += iterator.val

            # If the value of the new iterated node is 0, insert
            # running sum as value in inserter node, move inserter 
            # pointer, and reset current running sum
            if iterator.val == 0:
                inserter = inserter.next
                inserter.val = current
                current = 0
            
        # Remove and return the correct parts of the linked list
        inserter.next = None
        return head.next
