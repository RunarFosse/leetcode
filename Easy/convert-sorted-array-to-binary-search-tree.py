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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Using Divide and Conquer
        self.nums = nums
        return self.construct(0, len(nums)-1)
    
    def construct(self, start: int, end: int) -> Optional[TreeNode]:
        # Return empty if it is an empty interval
        if start > end:
            return None
        
        # If not, extract middle value, and construct subtrees on each side
        pivot = (start + end) // 2
        root = TreeNode(self.nums[pivot])
        root.left = self.construct(start, pivot-1)
        root.right = self.construct(pivot+1, end)

        # Return the full subtree
        return root
        
