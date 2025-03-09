# Author: Runar Fosse
# Time complexity: O(n + k)
# Space complexity: O(1)

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Using sliding window
        n = len(colors)

        # Store current number of groups, and the last element
        groups, last = 0, colors[0]

        # Slide a window over the colors array
        start, i = 0, 1
        while start < n and i < n + k:
            # If the color is non-alternating, reset window
            if colors[i % n] == last:
                start = i
            # Otherwise, if the window is full-sized, count it and shrink
            elif i + 1 - start == k:
                groups += 1
                start += 1

            # Expand the window
            last = colors[i % n]
            i += 1

        # Finally, return the number of alternating groups
        return groups
