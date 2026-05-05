# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If there are no rotations, or if the list is empty
        if k == 0 or head is None:
            # Return without modification
            return head

        # First, compute the length of the list, also storing last element
        n, last = 1, head
        while last.next:
            # By iterating the linked list and counting its elements
            last = last.next
            n += 1
        
        # Connect the end of the linked list to the head
        last.next = head
        
        # Then, compute the index of the last element after rotation
        i = n - 1 - (k % n)

        # Iterate to this last element
        current = head
        for _ in range(i):
            current = current.next
        
        # Cut the list in two, updating the head of the linked list
        head = current.next
        current.next = None

        # Finally, return this head element in the rotated list
        return head
