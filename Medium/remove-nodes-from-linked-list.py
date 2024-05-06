# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using DFS
        return self.dfs(head)[0]

    def dfs(self, head: Optional[ListNode]) -> (Optional[ListNode], int):
        # If we've reached the end of the list
        if not head:
            # Start returning list and max values
            return (None, 0)
        
        # If not, iterate and extract nodes to the right + their max values
        nodes, max_value = self.dfs(head.next)

        # Add current node to list if greater or equal to max_value
        if head.val >= max_value:
            head.next = nodes
            return (head, head.val)

        # If not, skip current node
        return (nodes, max_value)
