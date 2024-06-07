# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def checkRecord(self, s: str) -> bool:
        # Count total days absent, and consecutive days late
        absents, consecutive_lates = 0, 0
        for c in s:
            if c == "A":
                absents += 1
                # If absent more than 1 day, student is not eligible
                if absents > 1:
                    return False
            if c == "L":
                consecutive_lates += 1
                # If consecutively late for more than 2 days, not eligible
                if consecutive_lates > 2:
                    return False
            else:
                consecutive_lates = 0
        
        # If code above terminates, student is eligible for the reward!
        return True