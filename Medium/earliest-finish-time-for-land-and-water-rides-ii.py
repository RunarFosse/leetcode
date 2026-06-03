# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(1)

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # Using greedy
        m, n = len(landStartTime), len(waterStartTime)

        # First, compute the earliest time you can finish either a land ride or water ride
        landFinish, waterFinish = 1e9, 1e9
        for i in range(m):
            landFinish = min(landStartTime[i] + landDuration[i], landFinish)
        for j in range(n):
            waterFinish = min(waterStartTime[j] + waterDuration[j], waterFinish)
        
        # Then, compute the earliest you can finish both rides
        totalFinish = 1e9
        for i in range(m):
            totalFinish = min(max(landStartTime[i], waterFinish) + landDuration[i], totalFinish)
        for j in range(n):
            totalFinish = min(max(waterStartTime[j], landFinish) + waterDuration[j], totalFinish)
        
        # Finally, return this earliest finish time for both rides
        return totalFinish
