# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    mod = int(1e9 + 7)
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # Using dynamic programming
        opt = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]

        for i in range(zero + 1):
            for j in range(one + 1):
                for last in [0, 1]:
                    # Base cases
                    if i == 0:
                        opt[i][j][last] = 1 if j <= limit and last == 1 else 0
                        continue
                    if j == 0:
                        opt[i][j][last] = 1 if i <= limit and last == 0 else 0
                        continue
                    
                    # Recurrency
                    if last == 0:
                        arrays = sum(opt[i - 1][j])
                        if i > limit:
                            arrays -= opt[i - limit - 1][j][1]
                    else:
                        arrays = sum(opt[i][j - 1])
                        if j > limit:
                            arrays -= opt[i][j - limit - 1][0]
        
                    opt[i][j][last] = arrays % self.mod

        # Finally, return the number of all possible stable binary arrays
        return sum(opt[zero][one]) % self.mod


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