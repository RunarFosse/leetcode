# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Using two pointer
        n = len(arr)

        # Find the longest non-decreasing subarray from the left
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        # If left traverses the entire array, it is already sorted
        if left == n - 1:
            return 0

        # Otherwise, compute the longest non-decreasing subarray from the right
        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        
        # Otherwise, compute the shortest middle subarray to remove
        subarray = min(n - left - 1, right)
        start, end = 0, right
        while start <= left and end < n:
            if arr[start] <= arr[end]:
                subarray = min(end - start - 1, subarray)
                start += 1
            else:
                end += 1

        # Finally returning said shortest subarray to remove
        return subarray
