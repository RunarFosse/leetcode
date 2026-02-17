# Author: Runar Fosse
# Time complexity: O(10 choose n)
# Space complexity: O(1)

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Using bit manipulation

        # If there are no turned on numbers, return early
        if not turnedOn:
            return ["0:00"]

        # Initialize the first number with "turnedOn" bits
        on = (1 << turnedOn) - 1

        # Iterate every number with this same number of bits set
        times = []
        while on < (1 << 10):
            # Iterate the bits, computing its current time
            hours, minutes = on >> 6, on & ((1 << 6) - 1)

            # If the time is a valid time, add it to the list
            if hours < 12 and minutes < 60:
                times.append(f"{hours}:{minutes:02d}")

            # Using Gosper's hack, compute the next valid number
            r = (on & -on)
            t = on + r
            on = t | (((on ^ t) // r) >> 2)
        
        # Finally, return every valid time
        return times
