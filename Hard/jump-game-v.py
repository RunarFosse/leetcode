# Author: Runar Fosse
# Time complexity: O(nd)
# Space complexity: O(n)

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # Using dynamic programming
        self.n, self.arr, self.d = len(arr), arr, d
        return max(self.opt(i) for i in range(self.n))
    
    @functools.cache
    def opt(self, i: int) -> int:
        # We've already visited this initial node
        indices = 1

        # Iterate all jumpable indices rightwards
        for j in range(i + 1, min(i + self.d + 1, self.n)):
            if self.arr[j] >= self.arr[i]:
                break
            indices = max(1 + self.opt(j), indices)
        
        # Iterate all jumpable indices leftwards
        for j in reversed(range(max(i - self.d, 0), i)):
            if self.arr[j] >= self.arr[i]:
                break
            indices = max(1 + self.opt(j), indices)
        
        # Finally, return the number of visited indices
        return indices


# opt(i) - The maximum number of indices one can visit starting from index i

# Base case:
# opt(i) = 1            if arr[i] is a local minima

# Recurrency:
# opt(i) = 1 + max(
#                   opt(j) 
#                   for j in [i - d, i + d] \ {i} 
#                   if all(arr[j'] < arr[i] for j' in (i, j])
#               )

# N.o. states = n
# Time complexity per state -> O(d)
# Total time complexity => O(nd)