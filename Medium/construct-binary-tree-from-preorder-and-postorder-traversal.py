# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Using DFS
        self.preorder, self.postorder = deque(preorder), deque(postorder)
        return self.dfs()

    def dfs(self) -> TreeNode:
        # The current node is denoted by the first preorder element
        node = TreeNode(val = self.preorder.popleft())

        # If this element is equal to the first postorder traversal
        if node.val == self.postorder[0]:
            # Return upwards
            self.postorder.popleft()
            return node
        
        # Otherwise, continue downwards
        node.left = self.dfs()

        # Again, check if we should return upwards
        if node.val == self.postorder[0]:
            self.postorder.popleft()
            return node
        
        # Or downwards again
        node.right = self.dfs()

        # Finally, return upwards
        self.postorder.popleft()
        return node
