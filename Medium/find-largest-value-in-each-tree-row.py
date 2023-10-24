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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.largest = []
        self.dfs(root, 0)
        return self.largest
        
    def dfs(self, root: Optional[TreeNode], depth: int) -> None:
        if root:
            if len(self.largest) <= depth:
                self.largest.append(root.val)
            else:
                self.largest[depth] = max(root.val, self.largest[depth])
        
            self.dfs(root.left, depth+1)
            self.dfs(root.right, depth+1)