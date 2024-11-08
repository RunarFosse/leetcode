# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Calculate the XOR sum of the array
        xor_sum = reduce(lambda e, r: r ^ e, nums)

        # Store the largest possible query integer
        query_max = pow(2, maximumBit) - 1

        # Iterate the array in reverse order
        result = []
        for num in reversed(nums):
            # Compute the number which maximizes XOR for this query
            result.append(xor_sum ^ query_max)

            # And remove the last element from nums
            xor_sum ^= num

        # Return the result for each query
        return result