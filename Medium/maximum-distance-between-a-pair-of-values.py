# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(1)

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # Using two pointer
        m, n = len(nums1), len(nums2)

        # Iterate both arrays
        distance = 0
        i, j = 0, 0
        while i < m and j < n:
            # If we have a valid pair
            if nums1[i] <= nums2[j]:
                # Store the maximum distance
                distance = max(j - i, distance)

                # And increment right pointer
                j += 1
            else:
                # Otherwise, increment else pointer
                i += 1
        
        # Finally, return the maximum distance between valid pairs
        return distance
