# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Using greedy
        n = len(pattern)

        # Iterate the string
        decreasing = deque([0])
        for c in reversed(pattern):
            # And compute how many decreasing directly follows an index
            decreasing.appendleft(decreasing[0] + 1 if c == "D" else 0)
        
        # Then iterate this list
        number, current = [], 1
        for i in range(n+1):
            # The current number to be added is equal to the smallest
            # possible number, plus the current decreasing trend
            number.append(str(current + decreasing[i]))

            # If we are not decreasing, increment the current smallest
            if not decreasing[i]:
                current = i + 2
        
        # Finally, return the smallest possible number
        return "".join(number)

