# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        self.leftChild = leftChild
        self.rightChild = rightChild

        # Find no. parents per node
        hasParent = [False] * n
        for i in range(0, n):
            left, right = leftChild[i], rightChild[i]
            if left != -1:
                if hasParent[left]:
                    return False
                hasParent[left] = True
            if right != -1:
                if hasParent[right]:
                    return False
                hasParent[right] = True
        
        # Find root
        root = -1
        for i in range(0, n):
            if not hasParent[i]:
                root = i
        if root == -1:
            return False

        # Count nodes
        count = self.countNodes(root)
        return count == n
            
    def countNodes(self, i: int) -> (int, bool):
        descendants = 1
        left, right = self.leftChild[i], self.rightChild[i]
        if left != -1:
            descendants += self.countNodes(left)
        if right != -1:
            descendants += self.countNodes(right)
        return descendants


        
# This is yet another badly worded question:
# For a tree to form exactly one valid binary tree we need to ensure that:
# - There has to be exactly one source node, the root.
# - Every node has to have at most one parent.
# - The tree spans all nodes.

# First we find the root node, and at the same time keep track if any have more
# than one parent (-> invalid).
# After we have found the root (if no root -> invalid), we use DFS
# to count number of nodes in the tree (no. nodes != n -> invalid).