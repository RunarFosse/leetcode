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
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # Using DFS
        self.forest, self.to_delete = [], set(to_delete)
        self.forest.append(self.dfs(root))

        # Remove empty subtrees and return forest
        return filter(bool, self.forest)
    
    def dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # If we should delete current node, add children to forest
        if root.val in self.to_delete:
            self.forest.append(self.dfs(root.left))
            self.forest.append(self.dfs(root.right))
            return None
        
        # If not, continue DFS
        root.left = self.dfs(root.left)
        root.right = self.dfs(root.right)
        return root
