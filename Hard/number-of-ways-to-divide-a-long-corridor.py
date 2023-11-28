# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def numberOfWays(self, corridor: str) -> int:
        # First count number of seats, and store them with their indices
        seats = []
        for i, obstacle in enumerate(corridor):
            if obstacle == "S":
                seats.append(i)

        # If seats are zero or odd, we cannot divide
        if not seats or len(seats) % 2:
            return 0

        # Calculate the different "tight" segments containing strictly two seats
        segments = []
        last = None
        for seat in seats:
            if last != None:
                segments.append((last, seat))
                last = None
            else:
                last = seat

        # If there only exists one segment, the corridor is already maximally divided
        if len(segments) == 1:
            return 1
        
        # Then count the number of plants between any adjacent segments
        # This is where we can place a divider
        plants_between = []
        for i in range(1, len(segments)):
            plants_between.append(segments[i][0] - segments[i-1][1])
        
        # The number of possible valid divider positions are the product of these
        divides = 1
        for spots in plants_between:
            divides = (divides * spots) % self.mod

        return divides