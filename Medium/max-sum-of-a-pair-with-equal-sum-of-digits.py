# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(n)

# where m is the maximum size of a number

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        # Iterate over the numbers
        max_sum, seen = -1, {}
        for num in nums:
            # Compute the digit sum of the number
            digits = self.digitSum(num)

            # If we've seen this digit sum before
            if digits in seen:
                # Store maximum sum
                max_sum = max(seen[digits] + num, max_sum)
            
                # And store maximum number with current sum of digits
                seen[digits] = max(num, seen[digits])
            
            # If not, store number in seen
            else:
                seen[digits] = num

        # Return the maximum sum
        return max_sum
    
    def digitSum(self, num: int) -> int:
        # Compute the digit sum of a number
        total = 0
        while num:
            num, rem = divmod(num, 10)
            total += rem
        return total