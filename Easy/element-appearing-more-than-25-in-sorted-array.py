# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        for i in range(n-1):
            if arr[i] == arr[i+1]:
                count += 1 
            elif (count+1) * 4 > n:
                return arr[i]
            else:
                count = 0

        # If we have gone through the array without finding most frequent
        # number it is guaranteed to be the last.
        return arr[-1]