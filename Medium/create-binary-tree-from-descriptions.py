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
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Using DFS
        n = len(descriptions)
        
        # First iterate each description, counting indegree of each node,
        # as well as creating an adjacency list containing nodes [left, right]
        indegrees = defaultdict(int)
        self.adjls = defaultdict(lambda: [None, None])
        for parent, child, isLeft in descriptions:
            indegrees[child] += 1
            if isLeft:
                self.adjls[parent][0] = child
            else:
                self.adjls[parent][1] = child
        
        # Then create the tree using DFS
        root = next(node for node in self.adjls.keys() if not indegrees[node])
        return self.dfs(root)

    def dfs(self, root: Optional[int]) -> Optional[TreeNode]:
        # If root is None, return None
        if not root:
            return None

        # Create current subtree
        subtree = TreeNode(root)

        # Add subtrees of children
        subtree.left = self.dfs(self.adjls[root][0])
        subtree.right = self.dfs(self.adjls[root][1])

        # And return
        return subtree