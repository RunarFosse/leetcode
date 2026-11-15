# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def numOfWays(self, nums: list[int]) -> int:
        # Using Cartesian tree
        n = len(nums)

        # Record each element's insertion position
        position = [0] * n
        for i in range(n):
            position[nums[i] - 1] = i
        
        # Then, construct the BST using a Cartesian tree
        left, right, stack = [None] * n, [None] * n, []
        for element in range(n):
            # Remove all elements on the rightmost path inserted later than this element
            last = None
            while stack and position[stack[-1]] > position[element]:
                last = stack.pop()
            
            # If there still is an element on the stack
            if stack:
                # Make the current element the right child of that element
                right[stack[-1]] = element
            
            # If we've removed any elements from the rightmost path
            if last is not None:
                # Make the last one removed the left child of this element
                left[element] = last
            
            # And append the current element to the stack
            stack.append(element)
        
        # The root of the Cartesian tree is the first element of the stack
        root = stack[0]

        # Then, precompute factorials and their modular inverses
        factorial, inverse = [1] * n, [1] * n
        for i in range(1, n):
            factorial[i] = i * factorial[i - 1] % self.mod
        
        # Using Fermat's little theorem to compute the factorial modular inverses
        inverse[n - 1] = pow(factorial[n - 1], self.mod - 2, self.mod)
        for i in reversed(range(n - 1)):
            inverse[i] = (i + 1) * inverse[i + 1] % self.mod
        
        # Using DFS, compute the BST Cartesian tree traversal order
        order, stack = [], [root]
        while stack:
            node = stack.pop()
            order.append(node)
            if left[node] is not None:
                stack.append(left[node])
            if right[node] is not None:
                stack.append(right[node])

        # Then, count the BST reorderings from the bottom up
        size, ways = [0] * n, [1] * n
        for node in reversed(order):
            lefts = size[left[node]] if left[node] is not None else 0
            rights = size[right[node]] if right[node] is not None else 0

            # Update the size of the current node's subtree
            size[node] = lefts + rights + 1

            # Count the ways to interleave left and right subtree orderings
            reciprocal = (inverse[lefts] * inverse[rights]) % self.mod
            combinations = (factorial[lefts + rights] * reciprocal) % self.mod

            # And computing the total number of ways to reorder this subtrees array
            leftways = ways[left[node]] if left[node] is not None else 1
            rightways = ways[right[node]] if right[node] is not None else 1
            ways[node] = (combinations * leftways * rightways) % self.mod
        
        # Return the total number of ways to reorder the whole array preserving this BST
        return (ways[root] - 1) % self.mod
