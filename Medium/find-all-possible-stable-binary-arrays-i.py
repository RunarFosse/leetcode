# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    mod = int(1e9 + 7)
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # Using dynamic programming
        self.limit = limit
        arrays = self.opt(zero, one, 0) + self.opt(zero, one, 1)
        return arrays % self.mod
    
    @functools.cache
    def opt(self, i: int, j: int, last: int) -> int:
        # Base cases
        if i == 0:
            return 1 if j <= self.limit and last == 1 else 0
        if j == 0:
            return 1 if i <= self.limit and last == 0 else 0
        
        # Recurrency
        if last == 0:
            arrays = self.opt(i - 1, j, 0) + self.opt(i - 1, j, 1)
            if i > self.limit:
                arrays -= self.opt(i - self.limit - 1, j, 1)
        else:
            arrays = self.opt(i, j - 1, 0) + self.opt(i, j - 1, 1)
            if j > self.limit:
                arrays -= self.opt(i, j - self.limit - 1, 0)
        
        return arrays % self.mod


# opt(i, j, last) - The number of stable binary arrays with 'i' 0s and 'j' 1s
#                   with the final entry in the array being a 'last'.

# Base case:
# opt(0, j, 0) = 0
# opt(0, j, 1) = 1 if j <= limit else 0
# opt(i, 0, 0) = 1 if i <= limit else 0
# opt(i, 0, 1) = 0

# Recurrency:
# opt(i, j, last) | last == 0 = opt(i - 1, j, 0) + opt(i - 1, j, 1) 
#                               - (opt(i - limit - 1, j, 1) if i > limit else 0)
#                 | last == 1 = opt(i, j - 1, 0) + opt(i, j - 1, 1) 
#                               - (opt(i, j - limit - 1, 0) if j > limit else 0)

# N.o. states = m * n * 2
# Time complexity per state -> O(1)
# Total time complexity => O(mn)