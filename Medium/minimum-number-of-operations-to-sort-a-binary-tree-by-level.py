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
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # Using BFS
        operations = 0

        # If the tree is empty, return
        if not root:
            return operations

        # Iterate over the tree
        queue = deque([root])
        while queue:
            # First search 1 iteration downwards
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Then count inversions and add to operations
            operations += self.countInversions(queue)
        
        # Finally, return minimum number of operations
        return operations

    def countInversions(self, queue: List[TreeNode]) -> int:
        # Keep a sorted and unsorted list version
        unordered = list(map(lambda node: node.val, queue))
        ordered = sorted(unordered)

        # Store the current index of every element
        n = len(unordered)
        indices = {unordered[i]: i for i in range(n)}

        # Iterate the list
        inversions = 0
        for i in range(n):
            # If there is an inversion, swap positions
            if unordered[i] != ordered[i]:
                inversions += 1

                swap_index = indices[ordered[i]]
                indices[unordered[i]] = swap_index
                unordered[swap_index] = unordered[i]
        
        # Return the number of inversions
        return inversions
