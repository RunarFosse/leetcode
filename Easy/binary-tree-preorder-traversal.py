# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(log n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                continue

            # Add the node to preorder array
            preorder.append(node.val)

            # Add left and right children to queue, in preorder
            queue.appendleft(node.right)
            queue.appendleft(node.left)
        
        return preorder