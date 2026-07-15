# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Using arithmetic

        # First, compute both sumOdd and sumEven
        sumOdd = n * n
        sumEven = n * (n + 1)

        # Then, compute their GCD using the Euclidean algorithm
        a, b = sumEven, sumOdd
        while b != 0:
            a, b = b, a % b
        gcd = a

        # Finally, return this GCD
        return gcd


# The sum of the first n positive integers is given by:
# sum [1..n] = 1 + 2 + 3 + ... + n = (n * (n + 1)) // 2

# The sum of the n smallest positive even numbers is given by:
# 2 + 4 + 6 + ... + 2n = 2 * (1 + 2 + 3 + ... + n) = 2 * sum [1..n] = n * (n + 1)

# The sum of the n smallest odd numbers is given by:
# 1 + 3 + 5 + ... + 2n - 1 = sum [1..2n] - 2 * sum [1..n]
#                          = (2n * (2n + 1)) // 2 - n * (n + 1)
#                          = n * (2n + 1) - n * (n + 1)
#                          = n * (2n + 1 - (n + 1))
#                          = n * n

# Thus we can compute both sumOdd and sumEven in constant time.