# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # First, compute the angle of the hour and minute hand
        hour = hour * 30 + 0.5 * minutes
        minutes = minutes * 6

        # Compute the angle difference between the hands
        angle = abs(hour - minutes)

        # Finally, return the smaller opposite angle
        return min(angle, 360 - angle)


# The minute hand moves 6 degrees per minute.
# The hour hand moves 30 degrees per hour + 0.5 degrees per minute.

# Compute the difference and we have our angle.