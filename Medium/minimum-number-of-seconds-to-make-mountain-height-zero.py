# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Using heap

        # First, create a min-heap with the times for each of the workers
        workers = [(baseTime, baseTime, 1) for baseTime in workerTimes]
        heapify(workers)

        # Then, while the mountain is over zero height
        seconds = 0
        while mountainHeight:
            # Pick the worker that minimizes total time
            totalTime, baseTime, worked = heappop(workers)

            # Make the worker chisel a height off the mountain
            mountainHeight -= 1
            worked += 1

            # Store the maximum total time
            seconds = max(totalTime, seconds)

            # Compute their new total time
            totalTime += worked * baseTime

            # And add them back into the heap
            heappush(workers, (totalTime, baseTime, worked))
        
        # Finally, return the total time
        return seconds
