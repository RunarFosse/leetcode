# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Using sliding window
        n = len(nums)

        # Count the number of distinct elements in the array
        distincts = len(set(nums))

        # Then slide a window over the array
        completes = 0
        subarray, end = defaultdict(int), 0
        for start in range(n):
            # Expand the window until it is complete
            while end < n and len(subarray) < distincts:
                subarray[nums[end]] += 1
                end += 1
            
            # Then, count number of complete subarrays from this
            if len(subarray) == distincts:
                completes += n - end + 1
            
            # Then shrink the array
            subarray[nums[start]] -= 1
            if not subarray[nums[start]]:
                subarray.pop(nums[start])
        
        # Finally, return the total number of complete subarrays
        return completes
