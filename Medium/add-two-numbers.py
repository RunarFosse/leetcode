# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoHelper(l1, l2)
    
    def addTwoHelper(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
        if l1 == None:
            return self.addTwoHelper(ListNode(carry), l2) if carry else l2
        if l2 == None:
            return self.addTwoHelper(l1, ListNode(carry)) if carry else l1

        result = l1.val + l2.val + carry
        carry = 0

        if result > 9:
            result %= 10
            carry = 1
        
        return ListNode(result, self.addTwoHelper(l1.next, l2.next, carry))