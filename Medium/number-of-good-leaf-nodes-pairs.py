# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # Using DFS
        self.distance, self.good_leaves = distance, 0
        self.dfs(root)
        return self.good_leaves
    
    def dfs(self, root: TreeNode) -> List[int]:
        # Return empty list if this node is None
        if not root:
            return []

        # If it is a leaf, return distance to it
        if not (root.left or root.right):
            return [1]
        
        # Get distances to leaves left and right of root node
        lefts = self.dfs(root.left)
        rights = self.dfs(root.right)

        # Calculate good leaf pairs while merging
        leaves = []
        for left_distance in lefts:
            if left_distance < self.distance:
                leaves.append(left_distance + 1)

            for right_distance in rights:
                # As lists are sorted, we can do an early break
                # if we reach a node too far away to make pair good
                if left_distance + right_distance > self.distance:
                    break
                self.good_leaves += 1
        
        # Add right nodes as well
        for right_distance in rights:
            if right_distance < self.distance:
                leaves.append(right_distance + 1)

        # Return sorted, merged list
        return list(sorted(leaves))