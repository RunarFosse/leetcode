# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        counts = [0] * n

        # Iterate array, storing counts of maximum possible value
        for num in arr:
            counts[min(num-1, n-1)] += 1
        
        # Then find the maximum possible number you can create following constraints
        maximum = 0
        for i in range(n):
            maximum = min(maximum + counts[i], i+1)

        return maximum