# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Using greedy algorithm
        if not list1 and not list2:
            return None

        if list1 and (not list2 or list1.val < list2.val):
            head = list1
            head.next = self.mergeTwoLists(list1.next, list2)
        else:
            head = list2
            head.next = self.mergeTwoLists(list1, list2.next)

        return head