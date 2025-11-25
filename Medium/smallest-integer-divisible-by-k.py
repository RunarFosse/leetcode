# Author: Runar Fosse
# Time complexity: O(k)
# Space complexity: O(1)

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Iterate all possible remainders
        current = 0
        for i in range(k):
            # Update the number
            current = (current * 10 + 1) % k

            # If it is zero, then it is divisible by k
            if not current:
                return i + 1
        
        # If current never becomes zero, it cannot be divisible by k
        return -1


# Check the remainders of a number through 111...111 % k. If they repeat, even once,
# we have a repeating series. Thus, we only need to iterate until either:
# 1. We have a remainder of 0   -> divisible by k
# 2. We have a repeat remainder -> not divisible by k

# We also know that a number k can have at most k unique remainders.
# Thus, the maximum number of iterations is trivial.

# To simplify the problem, we can omit storing seen remainders, and just iterate
# k times, checking if the remainder ever becomes zero. Otherwise it has to repeat.