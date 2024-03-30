# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)

        good_subarrays = 0
        current_subarrays = 0

        frequencies = defaultdict(int)
        distincts = 0

        p1, p2 = 0, 0
        while p2 < n:
            # Expand the window to the right
            frequencies[nums[p2]] += 1
            if frequencies[nums[p2]] == 1:
                distincts += 1
            p2 += 1

            # If window contains more than k distincts, shrink it
            if distincts > k:
                frequencies[nums[p1]] -= 1
                if not frequencies[nums[p1]]:
                    distincts -= 1
                p1 += 1
                current_subarrays = 0
            
            # If contains k, count good subarrays
            if distincts == k:
                while frequencies[nums[p1]] > 1:
                    frequencies[nums[p1]] -= 1
                    p1 += 1
                    current_subarrays += 1
                good_subarrays += current_subarrays + 1
        
        # Return count of good subarrays
        return good_subarrays

