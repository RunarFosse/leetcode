# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Using greedy
        n = len(arrays)
        distance = 0

        # Iterate every array, storing previously seen min/max
        min_seen, max_seen = arrays[0][0], arrays[0][-1]
        for i in range(1, n):
            min_current, max_current = arrays[i][0], arrays[i][-1]

            # Then use previously seen values to calculate maximum distance
            distance = max(abs(min_seen - max_current), distance)
            distance = max(abs(min_current - max_seen), distance)

            # And update seen values
            min_seen = min(min_current, min_seen)
            max_seen = max(max_current, max_seen)

        # Return the maximum distance
        return distance