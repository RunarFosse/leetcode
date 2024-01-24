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
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.occurences = [ 0 ] * 9
        self.occurences[root.val-1] += 1
        return self.dfs(root)
    
    def dfs(self, root: Optional[TreeNode]) -> int:
        # If we are at the end of a path
        if not (root.left or root.right):
            if self.isPsuedoPalindromic(self.occurences):
                return 1
            return 0

        # Continue DFS on left and right side
        psuedo_palindromic_paths = 0
        if root.left:
            self.occurences[root.left.val-1] += 1
            psuedo_palindromic_paths += self.dfs(root.left)
            self.occurences[root.left.val-1] -= 1
        if root.right:
            self.occurences[root.right.val-1] += 1
            psuedo_palindromic_paths += self.dfs(root.right)
            self.occurences[root.right.val-1] -= 1
        
        return psuedo_palindromic_paths
    
    def isPsuedoPalindromic(self, occurences: List[int]) -> bool:
        contains_odd = False
        for occurence in occurences:
            # If the occurence is odd
            if occurence % 2:
                # Check if we've already had one odd occurence before
                if contains_odd:
                    # If so, path cannot be palindromic
                    return False
                # If not, continue
                contains_odd = True
        
        # If we are here, all occurences are even + maybe one odd
        return True
        
# We can count the occurences of each node on a path, and if we are at the end
# of a path and every occurence is a multiple of 2, and one optional occurence
# which is not, then the current path is a psuedo palindromic path.

# We can solve this easily using DFS.