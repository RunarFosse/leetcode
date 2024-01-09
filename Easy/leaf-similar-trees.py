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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        sequences = zip(self.getLeaves(root1), self.getLeaves(root2))
        return reduce(lambda b, s: b and (s[0] == s[1]), sequences, True)

    def getLeaves(self, root: Optional[TreeNode]) -> Iterator[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.right:
                queue.appendleft(node.right)
            if node.left:
                queue.appendleft(node.left)

            # If it is a leaf, yield its value
            if not (node.left or node.right):
                yield node.val
            
        # At the end, yield None to verify length of trees are the same
        yield None

# Create a generator which yields the next leaf from left to right (preorder),
# then we can iterate this for both trees, checking that each is equal.

# As we are using generators, we only use constant auxillary space, as we are
# generating each element of the sequence in "real time".
# The space and time complexity is bottlenecked by the traversal function.