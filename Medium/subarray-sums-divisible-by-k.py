# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(k)

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0

        # Initialize an array keeping track of
        # previously seen remainders from modulo k
        previous = [1] + [0] * (k-1)

        # We iterate the nums array, keeping a cumulative sum
        cumulation = 0
        for num in nums:
            cumulation += num

            # If this the value of cumulation % k has been seen before,
            # then this indicates that the sum of values in
            # between are a multiple of k!
            result += previous[cumulation % k]

            # Add an occurence of this remainder
            previous[cumulation % k] += 1
        
        return result