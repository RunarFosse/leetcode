# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Reverse second half of list
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        slow.next, slow = None, slow.next
        
        last, current = None, slow
        while current:
            temp = current.next
            current.next = last
            last = current
            current = temp
                
        # Intertwine both lists
        front, back = head, last
        while front:
            front.next, front = back, front.next
            if back:
                back.next, back = front, back.next

# First reverse half the linked list. Then we reorder the list in the
# wanted way by using two pointers.