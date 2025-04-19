# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # Using two pointers
        n = len(nums)

        # Count frequency of each number
        frequency = defaultdict(int)

        # And iterate the array
        subarrays, end = 0, 0
        for start in range(n):
            # While we don't have enough pairs
            while k > 0 and end < n:
                # Iterate the array and count entries
                frequency[nums[end]] += 1

                # Update number of pairs if possible and move pointer
                if frequency[nums[end]] > 1:
                    k -= frequency[nums[end]] - 1
                end += 1
            
            # Count number of valid subarrays if we have enough pairs
            if k <= 0:
                subarrays += n - (end - 1)
            
            # Finally, move start pointer and remove pairs
            if frequency[nums[start]] > 1:
                k += frequency[nums[start]] - 1
            frequency[nums[start]] -= 1
        
        # Return the number of good subarrays
        return subarrays
