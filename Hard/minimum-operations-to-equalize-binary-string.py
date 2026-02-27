# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # Using analytical solution
        n = len(s)

        # First, count the number of 0s in the string
        zeros = sum(1 for c in s if c == "0")

        # If there are no zeros, string is already equalized
        if not zeros:
            return 0
        
        # If k is equal to the length of the string
        if n == k:
            # Then the string is only equalizable if it is only zeros
            return 1 if zeros == n else -1

        # Compute the odd number of operations:
        # Flipping every zero, and skipping every one (at least once)
        odd = max(ceil(zeros / k), ceil((n - zeros) / (n - k)))
        if not odd % 2:
            odd += 1
        
        # Compute the even number of operations:
        # Flipping every zero, and skipping every zero (at least once)
        even = max(ceil(zeros / k), ceil(zeros / (n - k)))
        if even % 2:
            even += 1

        # Then, check if the odd solution is viable:
        # Which it is if k has the same parity as the number of zeros!
        operations = 1e9
        if k % 2 == zeros % 2:
            # If it is, store it if minimum
            operations = min(odd, operations)
        
        # Otherwise, check if the even solution is viable:
        # Which it is if we have an even number of zeros
        if not zeros % 2:
            # If it is, store it if minimum
            operations = min(even, operations)

        # If operations is not overriden, there is no solution
        return operations if operations < 1e9 else -1


# String 0 1
# ----------
# 0011 - 2 2
# 1101 - 1 3
# 1010 - 2 2
# 0100 - 3 1
# 1111 - 0 4

# We want to get rid of all the 0s. This means that with the initial 0 and 1 count:
# 1. Flip initial 0s an odd amount of times
# 2. Flip initial 1s an even amount of times

# At each operation, we have to flip k numbers.

# With an initial count of zeros a, we know that the total number of flips is:
# operations * k >= a           -> operations >= a / k

# For the initial count of ones b, we know that the total number of non-flips is:
# operations * (n - k) >= b     -> operations >= b / (n - k)

# We can write b as a function of a, giving the identity
# operations >= b / (n - k)    <-> operations >= (n - a) / (n - k)

# This number of operations can either be odd or even.
# Eliminating some early edgecases (like trivial solutions), for operations parity:
# If it is odd, then every initial 1 has to be "not flipped" at least once
# If it is even, then every initial 0 has to be "not flipped" at least once
# Lastly, operations * k must have the same parity as the number of zeros to
# be a possible equalizing solution!

# Thus, we compute the smallest possible number of operations, both being either odd
# or even, and then check if any gives a possible solution, picking the minimum one!