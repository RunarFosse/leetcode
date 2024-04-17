# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(nlog n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Using DFS

        # Depth-first search through and store every string
        queue = [("", root)]
        strings = []
        while queue:
            path, node = queue.pop()
            if not node:
                continue
            
            # Add node to path string
            path = chr(node.val + ord("a")) + path
            
            # If leaf, store final path string
            if not (node.left or node.right):
                strings.append(path)
                continue
            
            # If not, add children to queue
            queue.append((path, node.left))
            queue.append((path, node.right))
        
        # Return the smallest lexicographic string
        return min(strings)