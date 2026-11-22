# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        # Using dynamic programming

        # Sort the numbers in ascending order
        nums.sort()

        # Track the longest consecutive subsequences ending at the current value,
        # or at the current value incremented by 1
        consecutive, incremented = 1, 1

        # Iterate every difference of numbers
        maximum = 1
        for num1, num2 in pairwise(nums):
            match num2 - num1:
                case 0:
                    # If the two numbers are the same, we can increment this
                    # to make a consecutive and increasing subsequence
                    incremented = consecutive + 1
                case 1:
                    # If consecutive, both incremented and normal stay consecutive
                    consecutive += 1
                    incremented += 1
                case 2:
                    # If a difference of 2, we can use our previous incremented
                    # to stay consecutive
                    consecutive = incremented + 1

                    # However, we cannot increment this to get a consecutive subsequence
                    incremented = 1
                case _:
                    # For any other case, no consecutive sequence can be extended
                    consecutive, incremented = 1, 1
            
            # Store the maximum consecutive subsequence size with or without increments
            maximum = max(consecutive, incremented, maximum)
        
        # And return this maximum subsequence size
        return maximum


# By sorting the array in ascending order, we can simplify the process of finding
# consecutive increasing subsequences.

# opt(i, incremented) - The longest consecutive increasing subsequence ending at
#                       nums[i] + (1 if incremented else 0), using values up to index i.

# Base case:
# opt(0, _) = 1

# Recurrency:
# opt(i, False) | difference == 0 = opt(i - 1, False)
#               | difference == 1 = opt(i - 1, False) + 1
#               | difference == 2 = opt(i - 1, True) + 1
#               | otherwise       = 1
#                where difference = nums[i] - nums[i - 1]
# opt(i, True) | difference == 0 = opt(i - 1, False) + 1
#              | difference == 1 = opt(i - 1, True) + 1
#              | otherwise       = 1
#               where difference = nums[i] - nums[i - 1]

# The answer to this problem is the maximum such sequence over the whole array.

# No. states = 2 * n
# Time complexity per state -> O(1)
# Total time complexity of DP => O(n)

# Total space complexity can be reduced to O(1) using iterative, bottom-up
# dynamic programming, as we at each step only use the previous iteration's values!
# This reduces the DP space complexity to O(1), though space complexity is still
# dominated by the sorting step's O(n).