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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Using In-order tree traversal

        modes, modecount = [], 0
        num, count = None, 0
        for val in self.traverse(root):
            if val != num:
                # If num is THE current mode
                if count > modecount:
                    modes = [num]
                    modecount = count
                # Else if its A current mode
                elif count == modecount:
                    modes.append(num)

            # Count occurences
                num = val
                count = 1
            else:
                count += 1
        
        if count > modecount:
            modes = [num]
            modecount = count
        elif count == modecount:
            modes.append(num)

        return modes
    
    # Generator performing in-order traversal
    def traverse(self, root: Optional[TreeNode]) -> int:
        if root.left:
            yield from self.traverse(root.left)
    
        yield root.val

        if root.right:
            yield from self.traverse(root.right)
            

# This question is weirdly asked. How can one "do that without using any extra space?"
# when the problem requires returning a list, without having any existing lists?