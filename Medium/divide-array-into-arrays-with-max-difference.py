# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Using greedy
        nums.sort()
        n = len(nums)
        arrays = []

        # Iterate each subarray in the sorted array
        for i in range(0, n, 3):
            subarray = nums[i:i+3]
            # If it isn't valid, return []
            if max(subarray) - min(subarray) > k:
                return []
            arrays.append(subarray)
        
        # Return the divided array
        return arrays

# Time complexity is O(n) as each max() and min() call is called over
# a subarray of size 3, which we can reduce to constant runtime.