# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        # Create the uncontaminated binary tree, storing values in a set
        root.val = 0
        self.seen = set()
        self.uncontaminate(root)

    def find(self, target: int) -> bool:
        # Check if target is in the set
        return target in self.seen
        
    def uncontaminate(self, root: Optional[TreeNode]) -> None:
        # Remember current node value
        self.seen.add(root.val)

        # Uncontaminate left
        if root.left:
            root.left.val = 2 * root.val + 1
            self.uncontaminate(root.left)

        # And right subtrees
        if root.right:
            root.right.val = 2 * root.val + 2
            self.uncontaminate(root.right)
            

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)