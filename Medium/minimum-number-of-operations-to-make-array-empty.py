# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Count frequency of each num
        frequencies = defaultdict(lambda : 0)
        for num in nums:
            frequencies[num] += 1
        
        # Count operations to make array empty
        min_operations = 0
        for frequency in frequencies.values():
            # Cannot make array empty if number appears once
            if frequency == 1:
                return -1

            # Calculate remainder from integer division with 3
            # and extrapolate operations to remove number from array
            operations, remainder = divmod(frequency, 3)
            if remainder == 0:
                min_operations += operations
            else:
                min_operations += operations + 1
        
        return min_operations
        
# Count frequency of each number, and for each frequency:
# If it is not a "compound multiple" of 3 and 2, return -1. 
# We cannot make array empty. 
# However, any number except 1 is a "compound multiple" of 3 and 2!

# Therefore we only need to verify that any frequency is not == 1!
# If it is a multiple of 3, add said multiple to operations, 
# and remove from frequency.
# We check the remainder after removing all multiples of 3. 
# If it is 2, we obviously only need to remove a pair once.
# However, if it is 1, this also means that without 1 "3-removal", remainder would
# be 4, equalling 2 "2-removal" operations.
# Notice, in both of these cases, the total operations are equal to the
# "3-removal" operations + 1! 