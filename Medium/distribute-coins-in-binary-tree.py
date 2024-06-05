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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # Using DFS
        return self.dfs(root)[1]
    
    def dfs(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return (0, 0)

        # Count number of coins moved downwards for
        # children to have exactly one coin
        lcoins, lmoves = self.dfs(root.left)
        rcoins, rmoves = self.dfs(root.right)

        # Count how many coins we need to move from
        # parent to this to have exactly one coin
        coins = 1 - (root.val - lcoins - rcoins)

        # Return coins moved downwards + total number of moves
        return (coins, abs(coins) + lmoves + rmoves)
    

# Start from leaves, and move (positive or negative) coins upwards such
# that every node has exactly one coin.
        