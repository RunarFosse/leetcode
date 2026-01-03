# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def numOfWays(self, n: int) -> int:
        # Using binary exponentiation

        # Given the initial two matrices
        rows = [[6], [6]]
        transformation = [[2, 2], [2, 3]]

        # Using binary exponentiation, compute the full transformation matrix
        transformation_full = self.power(transformation, n - 1)

        # Finally, multiply them together and return the number of valid grids
        result = self.multiply(transformation_full, rows)
        return (result[0][0] + result[1][0]) % self.mod

    def multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        # Naively multiply two small matrices
        m, n, o = len(a), len(b), len(b[0])
        result = [[0] * o for _ in range(m)]
        for i in range(m):
            for j in range(o):
                for k in range(n):
                    result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % self.mod
        
        # And return the result
        return result
    
    def power(self, matrix: List[List[int]], exponent: int) -> List[List[int]]:
        # Perform binary exponentiation on a matrix to the power of exponent

        # Start with the identity matrix
        result = [[1, 0], [0, 1]]

        # And binary exponentiate them together
        while exponent:
            if exponent & 1:
                result = self.multiply(result, matrix)
            matrix = self.multiply(matrix, matrix)
            exponent //= 2
        
        # Finally returning the resulting matrix
        return result

# There are two ways to color a row:
# 1: A B C       and       2: A B A

# Initially, there are 6 possible rows of each:
# 1 -> A B C or A C B or B A C or B C A or C A B or C B A
# 2 -> A B A or A C A or B A B or B C B or C A C or C B C

# Given a 1 row, there can only be 2 possible following 2 rows:
# 1. A B C
# 2. B A B or B C B

# Given a 1 row, there can only be 2 possible following 1 rows:
# 1. A B C
# 2. B C A or C A B

# Given a 2 row, there can only be 2 possible following 1 rows:
# 1. A B A
# 2. B A C or C A B

# Given a 2 row, there can only be 3 possible following 2 rows:
# 1. A B A
# 2. B A B or B C B or C A C

# This makes the solution trivial, as we can iteratively compute the number of valid
# grids up until that row, using the formula:
# Number of 1 rows = 2 * Number of 1 rows + 2 * Number of 2 rows
# Number of 2 rows = 2 * Number of 1 rows + 3 * Number of 2 rows

# This can be written as a matrix multiplication equation:
# [ 1s_i ] = [ 2  2 ] [ 1s_{i-1} ]
# [ 2s_i ] = [ 2  3 ] [ 2s_{i-1} ]

# Using the initial number of rows we have:
# [ 1s_i ] = [ 2  2 ]^(n-1) [ 6 ]
# [ 2s_i ] = [ 2  3 ]       [ 6 ]

# And can be solved as a Binary Exponentiation problem in logarithmic time.