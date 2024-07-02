# Author: Runar Fosse
# Time complexity: O(n+m)
# Space complexity: O(1)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # First we count each occurence of elements in nums1
        frequencies = [0] * 1001
        for num in nums1:
            frequencies[num] += 1
        
        # Then iterate nums2, decrementing and adding elements with
        # positive frequency into the intersection array
        intersection = []
        for num in nums2:
            if frequencies[num]:
                frequencies[num] -= 1
                intersection.append(num)
        
        # Return the intersection
        return intersection
