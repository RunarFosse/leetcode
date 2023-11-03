# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Using dynamic programming
        height = len(triangle)
        opt = triangle

        for i in reversed(range(height-1)):
            for j in range(len(triangle[i])):
                opt[i][j] = min(opt[i+1][j], opt[i+1][j+1]) + triangle[i][j]
        
        return opt[0][0]

    
# For each "node" we have to traverse down every path, storing
# minimum path sum for each node

# opt(i, j) - minimum path sum for row i, index j 

# Base case:
# opt(tree height, j) = triangle[tree height][j]

# Recurrency:
# opt(i, j) = min(opt(i+1, j), opt(i+1, j+1)) + triangle[i][j]