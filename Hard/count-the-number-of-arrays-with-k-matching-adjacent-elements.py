# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # Using combinatorics

        # The first index has m choices for what value it can take
        first = m

        # Exactly k indices afterwards have to be equal to the last element
        identicals = self.choose(n - 1, k)

        # Lastly, the rest of the indices have to differ from the last element
        differing = self.modexp(m - 1, n - k - 1)

        # Finally, return the total number of good arrays
        return first * identicals * differing % self.mod

    def choose(self, n: int, r: int) -> int:
        # First compute all factorials up to n
        factorial = [1] * (n + 1)
        for i in range(n):
            factorial[i + 1] = (i + 1) * factorial[i] % self.mod
        
        # Then compute the inverse of all factorials up to n,
        # using Fermat's Little Theorem as our starting point
        inverse = [1] * (n + 1)
        inverse[n] = self.modexp(factorial[n], self.mod - 2)
        for i in reversed(range(n)):
            inverse[i] = (i + 1) * inverse[i + 1] % self.mod
        
        # Return n "choose r"
        return factorial[n] * inverse[r] * inverse[n - r] % self.mod
    
    def modexp(self, base: int, exp: int) -> int:
        # Fast modular exponentiation algorithm
        result = 1
        while exp:
            if exp & 1:
                result = result * base % self.mod
            base = base * base % self.mod
            exp >>= 1
        return result
