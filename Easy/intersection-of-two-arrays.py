# Author: Runar Fosse
# Time complexity: O(n+m)
# Space complexity: O(n)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Using set
        set1 = set(nums1)

        # Create the intersection with unique values
        intersection = []
        for num in nums2:
            if num in set1:
                intersection.append(num)
                set1.remove(num)
        
        return intersection