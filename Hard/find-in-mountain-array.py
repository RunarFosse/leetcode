# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(1)

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Using binary search

        # First search to find peak of mountain
        left, right  = 0, mountain_arr.length() - 1
        while left < right:
            pivot = (left + right) // 2
            n1, n2 = mountain_arr.get(pivot), mountain_arr.get(pivot + 1)
            gradient = n2 - n1

            if left == right - 1:
                break

            if gradient > 0:
                left = pivot
            else:
                right = pivot

        peak = right
        # If peak is target, just return
        if mountain_arr.get(peak) == target:
            return peak

        # Then search both left and right side searching for target
        # (First left side as we should return the smallest index)
        left, right = 0, peak
        while left < right:
            pivot = (left + right) // 2
            n = mountain_arr.get(pivot)

            if n == target:
                return pivot

            if left == right - 1:
                break
            
            if n < target:
                left = pivot
            else:
                right = pivot
        
        if mountain_arr.get(right) == target:
            return right
        
        # Search right side
        left, right = peak, mountain_arr.length() - 1
        while left < right:
            pivot = (left + right) // 2
            n = mountain_arr.get(pivot)

            if n == target:
                return pivot

            if left == right - 1:
                break
            
            if n > target:
                left = pivot
            else:
                right = pivot
        
        return right if mountain_arr.get(right) == target else -1