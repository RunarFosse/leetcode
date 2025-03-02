# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        array = []

        # While either array is not fully explored, merge
        pointer1, pointer2 = 0, 0
        while pointer1 < n and pointer2 < m:
            id1, value1 = nums1[pointer1]
            id2, value2 = nums2[pointer2]

            if id1 == id2:
                array.append([id1, value1 + value2])
                pointer1 += 1
                pointer2 += 1
            elif id1 < id2:
                array.append([id1, value1])
                pointer1 += 1
            else:
                array.append([id2, value2])
                pointer2 += 1
        
        # Add remaining part to array
        if pointer1 < n:
            array += nums1[pointer1:]
        if pointer2 < m:
            array += nums2[pointer2:]

        # And return it
        return array