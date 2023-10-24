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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # Using DFS
        largest = []
        queue = [(root, 0)]
        while queue:
            node, depth = queue.pop()
            if not node:
                continue

            if depth == len(largest):
                largest.append(node.val)
            else:
                largest[depth] = max(node.val, largest[depth])
            
            queue.append((node.left, depth+1))
            queue.append((node.right, depth+1))

        return largest