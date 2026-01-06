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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Using BFS

        # Iterate each layer at a time, storing maximum layer sum
        queue, layer = deque([root]), 1
        maximum = (0, -1e9)
        while queue:
            # Compute the sum of the current layer
            current = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                current += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # If the sum is maximum, store it
            if current > maximum[1]:
                maximum = (layer, current)
            
            # And continue to the next layer
            layer += 1

        # Finally, return the layer with the maximum level sum
        return maximum[0]
