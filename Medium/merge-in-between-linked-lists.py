# Author: Runar Fosse
# Time complexity: O(m+n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # First find start of removal
        head = list1
        for _ in range(a-1):
            head = head.next
        
        # Then remove all in-between
        start = head
        end = head
        for _ in range(a-1, b+1):
            end = end.next
        
        # Then connect the two lists
        start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end
        
        # Return the whole list
        return list1