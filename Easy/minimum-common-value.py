# Author: Runar Fosse
# Time complexity: O(m+n)
# Space complexity: O(1)

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Using two pointer approach
        p1, p2 = 0, 0
        while nums1[p1] != nums2[p2]:
            # Increment based on value
            if nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

            # If either goes out of bounds, no minimum common value exists
            if p1 == len(nums1) or p2 == len(nums2):
                return -1

        # Return the minimum common value
        return nums1[p1]


# If we have two pointers, initially pointing at the start of each array, we can
# increment the one pointing to the smallest value until they point towards equal values.
# This is our minimum common value.