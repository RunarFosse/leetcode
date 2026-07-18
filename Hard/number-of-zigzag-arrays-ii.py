# Author: Runar Fosse
# Time complexity: O(m^3log n)
# Space complexity: O(m^2)

class Solution:
    mod = int(1e9 + 7)
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # Using matrix exponentiation

        # First, declare the initial state vector
        m = r - l + 1
        opt = [[1] * m]

        # Then, generate the transition matrix
        T = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m - i - 1):
                T[i][j] = 1
        
        # Then, compute the full transition matrix
        T_full = self.modexp(T, n - 1)

        # Finally, compute the final state vector
        opt = self.multiply(opt, T_full)

        # And return sum of valid ZigZag arrays
        return 2 * sum(opt[0]) % self.mod
    
    def multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        # Multiply together two matrices
        l, w, o = len(a), len(a[0]), len(b[0])

        # By summing over multiplied cells
        result = [[0] * o for _ in range(l)]
        for i in range(l):
            for k in range(w):
                # Greedily skip cells that do not contribute
                cell = a[i][k]
                if not cell:
                    continue
                for j in range(o):
                    result[i][j] = (result[i][j] + cell * b[k][j]) % self.mod
        
        # And return the resulting matrix
        return result
    
    def modexp(self, base: List[List[int]], exp: int) -> List[List[int]]:
        # Exponentiate a square matrix using fast modular exponentiation
        m = len(base)

        # Initialize a resulting matrix as the identity matrix
        result = [[0] * m for _ in range(m)]
        for i in range(m):
            result[i][i] = 1

        # Then, exponentiate
        while exp:
            if exp & 1:
                result = self.multiply(result, base)
            exp >>= 1
            if exp:
                base = self.multiply(base, base)
        
        # And return the resulting exponentiated matrix
        return result


# From the last problem: https://leetcode.com/problems/number-of-zigzag-arrays-i
# we have two different state transition equations:
#
# Let opt0 be ZigZag arrays with decreasing last 2 elements, opt1 be increasing:
#
# opt0[i](end) = sum(opt1[i - 1](j) for all j > end)
# opt1[i](end) = sum(opt0[i - 1](j) for all j < end)

# Previously optimized via prefix sums, but can also be represented
# as the equations with transition matrices:
#
# opt0[i] = opt1[i - 1] * A
# opt1[i] = opt0[i - 1] * B
# 
# As a single, vectorized equation:
#
#                  [opt0[i]  opt1[i]] = [opt1[i - 1]  opt0[i - 1]] * [A  0, 0  B]
# (or without swapping state vectors) = [opt0[i - 1]  opt1[i - 1]] * [0  B, A  0]

# Given that the matrix A represents all values larger than the "current" (lower down
# in the vector), and matrix B represents all values smaller than the "current" (higher
# up in the vector). In other words, the matrices A and B 
# are respectively strictly lower- and upper-triangular matrices.

# i.e., for m = len([l, r]) = 4, then:
#
# A = [0  0  0  0]         B = [0  1  1  1]
#     [1  0  0  0]             [0  0  1  1]
#     [1  1  0  0]             [0  0  0  1]
#     [1  1  1  0]             [0  0  0  0]

# The matrix [0 B, A 0] is itself a matrix (call it T), and would for m = 4 look like:
#
# T = [0  0  0  0  0  1  1  1]
#     [0  0  0  0  0  0  1  1]
#     [0  0  0  0  0  0  0  1]
#     [0  0  0  0  0  0  0  0]
#     [0  0  0  0  0  0  0  0]
#     [1  0  0  0  0  0  0  0]
#     [1  1  0  0  0  0  0  0]
#     [1  1  1  0  0  0  0  0]

# This results in our step transition equation:
# [opt0[i]  opt1[i]] = [opt0[i - 1]  opt1[i - 1]] * T

# Fascinatingly, continued multiplication allows for larger steps:
# [opt0[i]  opt1[i]] = [opt0[i - 2]  opt1[i - 2]] * T * T
# [opt0[i]  opt1[i]] = [opt0[i - 4]  opt1[i - 4]] * T * T * T * T
# [opt0[i]  opt1[i]] = [opt0[i - 10]  opt1[i - 10]] * T^10

# From this, if we can compute T^(n - 1) we directly have:
# [opt0[n]  opt1[n]] = [opt0[1]  opt1[1]] * T^(n - 1)

# Luckily, computing T^(n - 1) can be done using modular matrix exponentiation,
# running in O(m^3log n) time.

# Additionally, following the same observation as in the previous problem, the 
# state vectors are also mirrored in regards to the previous step's ZigZag slope.
# Thus we can utilize only 1 state vector piece opt, and thus we can reduce the
# respective initial transition matrix accordingly as well.
# We can also omit an explicit reversal step, as the reduced transition matrix
# encodes that implicitly.

# Example, for m = 4, our reduced transition matrix is now:
# T = [1  1  1  0]
#     [1  1  0  0]
#     [1  0  0  0]
#     [0  0  0  0]
#
# Multiplying with a state vector opt = [a, b, c, d] our result becomes:
# opt * T = [a + b + c, a + b, a, 0] 
# which is our prefix sum vector from the first problem,
# with the results already stored in reversed order!