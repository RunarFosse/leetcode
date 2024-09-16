# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Using bucket sort
        buckets = [False] * (24 * 60)

        # Turn string of time into minutes and sort into buckets
        toMinutes = lambda s: int(s[:2]) * 60 + int(s[3:])
        for time in timePoints:
            minutes = toMinutes(time)

            # If this time is already seen, minimum difference is 0
            if buckets[minutes]:
                return 0
            buckets[minutes] = True
        
        # Then iterate every bucket, keeping track of minimum time difference
        # between every two pair of times
        firstTime, lastTime = None, None
        minDifference = 24*60
        for time in range(24*60):
            if not buckets[time]:
                continue

            if firstTime is not None:
                lastDiff = min(time - lastTime, 1440 - (time - lastTime))
                firstDiff = min(time - firstTime, 1440 - (time - firstTime))
                minDifference = min(lastDiff, firstDiff, minDifference)

            if firstTime is None:
                firstTime = time
            lastTime = time

        # At last return the minimum time difference
        return minDifference
