# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Using two pointer approach

        # First find the length of the linked list
        n = 0
        current = head
        while current:
            current = current.next
            n += 1
        
        # Then reverse the second half of the list
        i = 0
        last, current = None, head
        while current:
            i += 1
            # If in first half, only iterate
            if i <= n//2:
                last = current
                current = current.next
            # Else in second, flip links
            else:
                temp = current.next
                current.next, last = last, current
                current = temp
            

        # Then check if list is palindromic using two pointers
        lp, rp = 0, n-1
        left, right = head, last
        while lp <= rp:
            if left.val != right.val:
                return False
            lp += 1
            rp -= 1
            left = left.next
            right = right.next
        
        return True
        
# To check if the linked list is palindromic we reverse the second half of 
# the list. Then we can iterate both parts towards the center and check
# if it is a palindrome using a two pointer approach.