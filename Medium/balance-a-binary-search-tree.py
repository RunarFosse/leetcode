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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Using DFS

        # First turn the binary search tree into a sorted array
        self.tree = []
        self.dfs(root)

        # Then reconstruct binary search tree from sorted array
        return self.construct(0, len(self.tree)-1)

    def dfs(self, node: TreeNode) -> None:
        # Perform in-order traversal and add to tree
        if (node.left):
            self.dfs(node.left)
        self.tree.append(node.val)
        if (node.right):
            self.dfs(node.right)
    
    def construct(self, i: int, j: int) -> TreeNode:
        # Early return if interval is empty
        if i > j:
            return None

        # First use the middle element in the interval as our subtree root
        pivot = (i+j) // 2
        root = TreeNode(self.tree[pivot])

        # Then construct left and right subtree from these
        root.left = self.construct(i, pivot-1)
        root.right = self.construct(pivot+1, j)

        # Finally return the whole subtree
        return root
    