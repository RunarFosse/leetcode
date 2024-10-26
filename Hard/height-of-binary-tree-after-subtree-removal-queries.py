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
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Using DFS

        # First precompute the height of the tree for any possible query
        self.heightsWithout = {}
        self.calculateHeightsWithout(root, 0, 0)

        # Then return the precomputed tree height for each query
        return [self.heightsWithout[query] for query in queries]

    @functools.cache
    def dfs(self, root: Optional[TreeNode]) -> int:
        # If we are at the end of a subtree, return
        if not root:
            return 0
        
        # If not, calculate the height of the current subtree and return
        return max(self.dfs(root.left), self.dfs(root.right)) + 1

    def calculateHeightsWithout(self, root: Optional[TreeNode], depth: int, other_height: int) -> None:
        # For this node, calculate height of tree without it
        self.heightsWithout[root.val] = other_height

        # Compute the heights of the lower subtrees
        left_height = self.dfs(root.left) + depth
        right_height = self.dfs(root.right) + depth

        # And recurse downwards
        if root.left:
            self.calculateHeightsWithout(root.left, depth + 1, max(right_height, other_height))
        if root.right:
            self.calculateHeightsWithout(root.right, depth + 1, max(left_height, other_height))