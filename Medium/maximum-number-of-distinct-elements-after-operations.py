# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # Using greedy

        # Sort the numbers in ascending order
        nums.sort()

        # Iterate the numbers
        distincts, last = 0, -k
        for num in nums:
            # If we cannot make this number distinct, continue
            if num + k <= last:
                continue
            
            # Otherwise, make it distinct
            last = max(last + 1, num - k)
            distincts += 1

        # Finally, return the number of distinct elements
        return distincts