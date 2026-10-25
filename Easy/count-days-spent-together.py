# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # First, compute the prefix month to days
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.monthToDays = list(accumulate(months, initial=0))
        
        # Then, get the day count of Alice and Bob's key arrival and departure days
        alice = (self.dateToDays(arriveAlice), self.dateToDays(leaveAlice))
        bob = (self.dateToDays(arriveBob), self.dateToDays(leaveBob))

        # Compute the intersection
        intersection = (max(alice[0], bob[0]), min(alice[1], bob[1]))

        # And return the total number of days of this intersection
        return max(intersection[1] - intersection[0] + 1, 0)

    def dateToDays(self, date: str) -> int:
        month, day = int(date[:2]), int(date[3:])
        return day + self.monthToDays[month - 1]
