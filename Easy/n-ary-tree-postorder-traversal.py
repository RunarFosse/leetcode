# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Using DFS
        traversal = []
        self.dfs(root, traversal)
        return traversal
    
    def dfs(self, root: 'Node', traversal: List[int]) -> None:
        if not root:
            return
        
        # First traverse children
        for child in root.children:
            self.dfs(child, traversal)

        # Then add current visited node to traversal array
        traversal.append(root.val)