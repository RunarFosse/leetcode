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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Using BFS
        queuep, queueq = [(p, 0)], [(q, 0)]
        while queuep and queueq:
            nodep, depthp = queuep.pop(0)
            nodeq, depthq = queueq.pop(0)

            if not nodep or not nodeq: # If any are None, only continue if both are
                if nodep or nodeq:
                    return False
                continue
            if nodep.val != nodeq.val or depthp != depthq:
                return False
            
            queuep.append((nodep.left, depthp+1))
            queuep.append((nodep.right, depthp+1))

            queueq.append((nodeq.left, depthq+1))
            queueq.append((nodeq.right, depthq+1))

        return len(queuep) == len(queueq) # == 0