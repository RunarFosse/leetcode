# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Using min-heap
        n = len(times)

        # Add index and sort the times by arrival time in ascending order
        times = sorted((times[i], i) for i in range(n))

        # Store free and occupied seats in separate min-heaps
        free, occupied = [i for i in range(n)], []
        for (arrives, leaves), i in times:
            # First move any no-longer-occupied chairs into the free heap
            while occupied and occupied[0][0] <= arrives:
                _, chair = heappop(occupied)
                heappush(free, chair)
            
            # Then occupy the smallest free chair
            chair = heappop(free)
            heappush(occupied, (leaves, chair))

            # If we are at the target friend, return the chair
            if i == targetFriend:
                return chair