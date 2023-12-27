# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Using sliding window
        timecost = 0

        p0, p1 = 0, 1
        while p0 < len(colors) - 1:
            # Find total sequence of equal colors
            while p1 < len(colors) and colors[p0] == colors[p1]:
                p1 += 1
            
            # Continue if the sequence only consists of one balloon
            if p0 == p1:
                p0 += 1
                p1 += 1
                continue
            
            # Otherwise, remove the balloons taking the smallest amount.
            # (This would be equal to removing all, but adding back balloon of max time.)
            maxTime = 0
            for p in range(p0, p1):
                timecost += neededTime[p]
                maxTime = max(neededTime[p], maxTime)
            timecost -= maxTime

            # Move first pointer location to second pointer
            p0 = p1
        
        return timecost

# Iterate the color list, finding sequences of consecutive balloons of the same color.
# If we find any such sequences, remove the minimum time balloon until there only exist one.