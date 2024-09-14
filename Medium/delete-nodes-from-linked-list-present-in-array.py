# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Using DFS

        # First turn the nums array into a set
        nums = set(nums)

        # Then iterate the linked list
        root, current = None, None
        while head:
            # If a node value is in nums, skip it
            if head.val in nums:
                head = head.next
                continue

            # If not, add it to the new linked list
            if not root:
                root = head
                current = root
            else:
                current.next = head
                current = current.next
            head = head.next
            current.next = None

        # Return the new filtered list
        return root