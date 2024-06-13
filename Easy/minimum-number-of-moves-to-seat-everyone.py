# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Using greedy
        n = len(seats)

        # Sort both seats and students in ascending order
        seats.sort()
        students.sort()

        # Then count number of moves to move student i to seats[i]
        return sum(abs(seats[i] - students[i]) for i in range(n))