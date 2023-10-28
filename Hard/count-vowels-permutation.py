# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = int(1e9 + 7)
        a = e = i = o = u = 1
        for _ in range(1, n):
            a, e, i, o, u = (e+i+u)%mod, (a+i)%mod, (e+o)%mod, i%mod, (i+o)%mod
        
        return (a + e + i + o + u) % mod

# Note after solving with dynamic programming:
# As the whole problem is solved using iterative summation of the previous
# iteration's value, it is obvious that we can reformat the solution in a much
# more efficient way.
# Instead of storing each iteration's values, we can use temporary values
# (or python's a,b,c = b,c,a) to iteratively calculate the answer in O(1) space.

# Store the number of strings ending in the given character as variables
# for _ in range(n), iteratively update these.
# The solution will be sum of these, modulo!


# opt(i, c) - number of strings of length n ending in character c

# Base case:
# opt(1, c) = 1

# Recurrency:
# opt(i, 'a') = opt(i-1, 'e') + opt(i-1, 'i') + opt(i-1, 'u')
# opt(i, 'e') = opt(i-1, 'a') + opt(i-1, 'i')
# opt(i, 'i') = opt(i-1, 'e') + opt(i-1, 'o')
# opt(i, 'o') = opt(i-1, 'i')
# opt(i, 'u') = opt(i-1, 'i') + opt(i-1, 'o')