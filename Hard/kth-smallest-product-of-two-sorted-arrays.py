# Author: Runar Fosse
# Time complexity: O(nlog mlog k)
# Space complexity: O(1)

# where k is the difference between minimum and maximum product of both arrays

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Using binary search

        # With all possible boundary products from the arrays
        boundaries = (nums1[0] * nums2[0], 
                      nums1[0] * nums2[-1], 
                      nums1[-1] * nums2[0], 
                      nums1[-1] * nums2[-1])

        # Binary search the k'th smallest product
        left, right = min(boundaries), max(boundaries)
        while left < right:
            pivot = (left + right) // 2
            # Count how many products are smaller or equal
            count = 0
            for num1 in nums1:
                # Using binary search
                if num1 == 0:
                    count += len(nums2) if pivot >= 0 else 0
                elif num1 > 0:
                    count += bisect_right(nums2, pivot / num1)
                else:
                    count += len(nums2) - bisect_left(nums2, pivot / num1)

            # And move bounds accordingly
            if count < k:
                left = pivot + 1
            elif count >= k:
                right = pivot
        return left