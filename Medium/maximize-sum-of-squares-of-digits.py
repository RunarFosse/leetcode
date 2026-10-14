# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Using greedy

        # Compute the remainder and division of sum by nine
        nines, remainder = divmod(sum, 9)

        # If this total number of digits require more than num
        digits = nines + (1 if remainder != 0 else 0)
        if digits > num:
            # Then there does not exist any good integers
            return ""
        
        # Otherwise, construct and return this good integer maximizing the score
        number = ["9"] * nines
        if nines < num:
            number += [str(remainder)] + ["0"] * (num - nines - 1)
        return "".join(number)


# This problem asks us to find the number which contains num digits,
# and where the sum of the digits equals sum,
# which maximizes the summed square of these digits.

# We can greedily compute this number by filling the leftmost digits in the
# number by the largest possible digits, until it equals the sum.
# If we need more than num digits for this to be possible, then there exists no
# such number which maximizes the summed square.

# This largest possible digit we're talking about is obviously 9, meaning the
# resulting number will take this form:
# "9" * x + (a remainder digit) + "0" * (num - x - 1)

# We can easily figure out how many 9s we can use by checking how many 9s the sum
# consists of, this will also give us the remainder digit!
# All in all, it trivializes our problem.