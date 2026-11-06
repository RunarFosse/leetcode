# Author: Runar Fosse
# Time complexity: O((m + n)log m)
# Space complexity: O(m)

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # Using binary search
        n, m = len(arr1), len(arr2)

        # Sort the second array in ascending order
        arr2.sort()

        # Then, iterate every value in the first array
        distance = 0
        for num in arr1:
            # Binary search the first value equal to or larger than (num - d)
            index = bisect_left(arr2, num - d)

            # If this element is larger than (num + d)
            if index == m or arr2[index] > num + d:
                # Then there is no element within distance d of nums
                distance += 1

        # Return the distance between the arrays
        return distance
