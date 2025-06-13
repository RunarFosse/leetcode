# Author: Runar Fosse
# Time complexity: O(n(log m + log n))
# Space complexity: O(1)

# where m denotes the maximum difference of elements the array

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Using binary search
        n = len(nums)

        # First, sort the array in ascending order
        nums.sort()

        # Then, binary search the minimum maximum difference of p pairs
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            pivot = (left + right) // 2

            # Check if we have p pairs with difference less than or equal to pivot
            i, pairs = 0, 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= pivot:
                    pairs += 1
                    i += 1
                i += 1
            
            # Move pointers accordingly
            if pairs >= p:
                right = pivot
            else:
                left = pivot + 1
        
        # Finally, return the minimum maximum difference of p pairs
        return left
