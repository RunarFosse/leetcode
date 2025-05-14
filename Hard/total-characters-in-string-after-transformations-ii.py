# Author: Runar Fosse
# Time complexity: O(n + log t)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # Using matrix multiplication

        # First, compute the transformation matrix
        transformation = Matrix(26, self.mod)
        for i in range(26):
            for j in range(1, nums[i] + 1):
                transformation.values[(i + j) % 26][i] = 1
        
        # Then, compute the transformation matrix for t transformations
        transformations = self.exponentiate(transformation, t)

        # Count the frequency of each letter
        indexOf = lambda c: ord(c) - ord("a")
        frequencies = [0] * 26
        for c in s:
            frequencies[indexOf(c)] += 1
        
        # And apply the final transformation matrix and count total characters
        chars = 0
        for i in range(26):
            for j in range(26):
                chars = (
                    chars + frequencies[j] * transformations.values[i][j]
                    ) % self.mod
        return chars
    
    def exponentiate(self, matrix: "Matrix", t: int) -> "Matrix":
        # Using fast exponentiation
        result = Matrix(26, self.mod, 0)
        for i in range(26):
            result.values[i][i] = 1

        while t:
            if t & 1:
                result *= matrix
            matrix *= matrix
            t >>= 1
        return result
        
class Matrix:
    def __init__(self, n: int, mod: int, value: int = 0):
        self.n = n
        self.mod = mod
        self.values = [[value] * n for _ in range(n)]
    
    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.n != other.n:
            raise Exception(f"Cannot multiply dim {self.n} with dim {other.n}")

        matrix = Matrix(self.n, self.mod, 0)
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    matrix.values[i][j] = (
                        matrix.values[i][j] + 
                        self.values[i][k] * other.values[k][j]
                        ) % self.mod 
        return matrix

# We can model the nums array as a transformation matrix, with iteratively
# applied transformations as matrix multiplications. By using matrix 
# exponentiation we can efficiently compute the transformation matrix
# needed for t iterative transformations!