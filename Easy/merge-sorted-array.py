# Author: Runar Fosse
# Time complexity: O(n+m)
# Space complexity: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, i = m-1, n-1, m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
        
        while i >= 0:
            if p1 >= 0:
                nums1[i] = nums1[p1]
                p1 -= 1  
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1

        
# Inversely sort in opposite order from behind
