# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # Using dynamic programming
        n, self.nums = len(nums), nums
        if n % 2 == 0:
            return True
        
        # Compute the maximum score surplus the first player can acquire over the second
        difference = self.opt(0, n - 1)

        # If score difference is positive, or it is a tie, then the first player wins
        return difference >= 0
    
    @functools.cache
    def opt(self, i: int, j: int) -> int:
        # If the interval is a singleton
        if i == j:
            # Return the value of the only element
            return self.nums[i]

        # Otherwise, pick the element resulting in the largest score    
        return max(self.nums[i] - self.opt(i + 1, j), self.nums[j] - self.opt(i, j - 1))


# opt(i, j) - The maximum score difference the next picking player can acquire over
#             the other by selecting from the array partitioned from index i to index j.

# Base case:
# opt(i, i) = nums[i]

# Recurrency:
# opt(i, j) = max(nums[i] - opt(i + 1, j), nums[j] - opt(i, j - 1))

# No. states = n * n
# Time complexity per state -> O(1)
# Total time complexity => O(n^2)

# Observation: 
# If the array is of even initial length, the first player can force their selection
# of either all even indexed elements, or odd indexed elements.
# 
# Take the array with indices 1, 2, 3, 4.
# Force evens: Pick 4, next picks either 1 or 3, force pick 2.
# Force odds: Pick 1, next picks either 2 or 4, force pick 3.
#
# By selecting evens or odds based on which has the maximal sum,
# the first player always wins.