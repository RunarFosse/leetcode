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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # Using BFS

        # Iterate each row seperately
        queue = deque([root])
        row_index = 0
        while queue:
            # Iterate each element in the current row
            last_val = 1e9 if row_index % 2 else -1e9
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                
                # Verify constraint given row index parity
                if row_index % 2:
                    if node.val % 2 or node.val >= last_val:
                        return False
                else:
                    if not node.val % 2 or node.val <= last_val:
                        return False
                
                # Update last_val
                last_val = node.val
                
                # Add all children to next row queue
                queue.append(node.left)
                queue.append(node.right)
            
            # Increment row index
            row_index += 1

        # If we reach this point, tree is Even-Odd
        return True
