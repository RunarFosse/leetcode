# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # Iterate the linked list
        number = 0
        while head:
            # Left shifting the bits in the number for each new entry
            number = (number << 1) + head.val
            head = head.next
        
        # Finally, return the decimal number
        return number