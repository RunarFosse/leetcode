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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Using inorder traversal
        queue = deque([root])
        path, visited = [], set()
        while queue:
            node = queue.popleft()
            if not node:
                continue
            
            # If node is visited, add it to path and continue
            if node in visited:
                path.append(node.val)
                continue
            
            visited.add(node)
            
            # Add nodes to queue inorderly
            queue.appendleft(node.right)
            queue.appendleft(node)
            queue.appendleft(node.left)
        
        return path