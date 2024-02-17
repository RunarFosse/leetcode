# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Using greedy
        jumps, n = [], len(heights)
        heapify(jumps)
        for i in range(1, n):
            difference = heights[i] - heights[i-1]

            # Check if we have to build
            if difference <= 0:
                continue

            # Use ladders for jump (by default)
            if ladders:
                heappush(jumps, difference)
                ladders -= 1
            # Use bricks for jump
            elif not jumps or difference < jumps[0]:
                bricks -= difference
            # "Repay" previous ladder usage
            else:
                bricks -= heappop(jumps)
                heappush(jumps, difference)
            
            # If bricks now is negative, we have reached our end
            if bricks < 0:
                return i-1

        # If we finish the for-loop, we've reached the end
        return n-1

# We know that it is best to use bricks on the lowest jumps and ladders on the
# highest.

# Iterate the array from left to right, assuming we should use ladders each 
# time, but storing the height of these jumps in a priority queue (min-heap).
# Then, if we ever find a jump which is bigger than the smallest jump used
# we previously used a ladder for, we "repay" the value of the ladder in bricks
# and "reuse" it (if we can).