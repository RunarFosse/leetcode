# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Using counting sort

        # First count frequency of each element in arr1
        frequencies = [0] * 1001
        for num in arr1:
            frequencies[num] += 1
        
        # Then iterate arr2, "sorting" arr1 in the correct order
        pointer = 0
        for num in arr2:
            while frequencies[num]:
                arr1[pointer] = num
                frequencies[num] -= 1
                pointer += 1
        
        # At last, we fill the remaining numbers in in ascending order
        for num in range(1001):
            while frequencies[num]:
                arr1[pointer] = num
                frequencies[num] -= 1
                pointer += 1
        
        # Finally, return the sorted arr1
        return arr1
