# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(n)

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Using math
        m = len(rolls)

        # Calculate the sum of the n missing rolls
        missing_sum = mean * (n + m) - sum(rolls)

        # If this sum is less than the number of dice rolls, or more
        # than what you get from only rolling 6s, then it is impossible
        if missing_sum < n or missing_sum > 6*n:
            return []
        
        # If not, distribute the mean over the missing rolls
        missing_rolls = [missing_sum // n] * n

        # And add the remainder to first rolls
        for i in range(missing_sum % n):
            missing_rolls[i] += 1
        
        # Return the missing rolls
        return missing_rolls


# mean = (sum(rolls_m) + sum(rolls_n)) / (n + m)
# From this we can deduce that:

# sum(rolls_n) = mean * (n + m) - sum(rolls_m)

# Then we simply check if we can find n integers between 1 and 6
# such that their sum equals sum(rolls_n). 