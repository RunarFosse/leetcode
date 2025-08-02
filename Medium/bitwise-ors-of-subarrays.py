# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # Iterate the array
        current, result = set(), set()
        for num in arr:
            # Add num to all previous ORs
            current = {num | or_sum for or_sum in current}

            # As well as starting a new subarray OR sum
            current.add(num)

            # And add all current OR sums to result
            result |= current

        # Finally, return result count of unique OR sums
        return len(result)

# Time complexity is bounded by O(n) as set of OR sums
# is monotonicly increasing, bounding which elements 
# it can contain, and ultimately giving the total
# iteration time of at most O(32), for a 32-bit number
        