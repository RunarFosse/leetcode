# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Using Binary Index Tree
        n = len(nums1)

        # First, store the index in nums2 of elements in nums1
        indices, indices2 = [0] * n, [0] * n
        for i in range(n):
            indices2[nums2[i]] = i
        for i in range(n):
            indices[indices2[nums1[i]]] = i
        
        # Then, create a binary index tree and iterate every index
        good, tree = 0, BinaryIndexTree(n)
        for i in range(n):
            # Find the position of nums1[i] in nums2
            position = indices[i]

            # Count how many elements are to the left and right in both arrays
            left = tree.sum(position)
            right = (n - position - 1) - (i - left)

            # Update the tree to include the current element
            tree.increase(position, 1)

            # And count all permutations of left and right elements as good
            good += left * right
        
        # Finally, return all good triplets
        return good

        
class BinaryIndexTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def increase(self, i: int, delta: int) -> None:
        # Iterate the tree downwards
        i += 1
        while i <= self.n:
            # Increase the value at the current step
            self.tree[i] += delta

            # Add 1 to the rightmost bit
            i += i & -i
    
    def sum(self, i: int) -> int:
        result = 0
        # Iterate the tree upwards
        i += 1
        while i > 0:
            # Summing values higher up
            result += self.tree[i]

            # Setting the rightmost bit to 0
            i -= i & -i
        return result
        