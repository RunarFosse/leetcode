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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Using BFS
        sums = []

        # Iterate the tree using BFS, storing the sum at every level
        queue = deque([root])
        while queue:
            # Compute and store the current level sum
            sums.append(0)
            for _ in range(len(queue)):
                node = queue.popleft()

                # Add current node to level sum
                sums[-1] += node.val

                # And add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        # At last, sort and return the k'th largest level sum, if it exists
        sums.sort(reverse=True)
        return -1 if len(sums) < k else sums[k - 1]