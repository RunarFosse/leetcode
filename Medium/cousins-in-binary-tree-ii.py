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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Using BFS
        
        # First, BFS the tree and store row-wise sums
        rows, queue = [], deque([root])
        while queue:
            rows.append(0)
            for _ in range(len(queue)):
                node = queue.popleft()

                # Store the sum of the current row
                rows[-1] += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        # Then perform BFS again, over each of the rows
        queue = deque([(root, 0)])
        for i in range(len(rows)):
            for _ in range(len(queue)):
                node, sibling = queue.popleft()

                # And set value to sum of other cousins
                node.val = rows[i] - node.val - sibling

                if node.left:
                    queue.append((node.left, node.right.val if node.right else 0))
                if node.right:
                    queue.append((node.right, node.left.val if node.left else 0))
        
        # Finally, return the new tree
        return root
        