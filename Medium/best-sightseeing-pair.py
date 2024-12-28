# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        # Maximize the sightseeing equation in one pass
        max_score, max_spot = 0, values[0]
        for j in range(1, n):
            max_score = max(max_spot + values[j] - j, max_score)
            max_spot = max(values[j] + j, max_spot)
        
        return max_score

# The sightseeing equation is given by:
# for i < j, values[i] + values[j] + i - j 