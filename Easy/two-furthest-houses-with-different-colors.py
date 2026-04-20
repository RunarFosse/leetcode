# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # Using greedy
        n = len(colors)

        # First, find the index and colour of the two first different coloured houses
        first = (colors[0], 0)
        second = next((colors[i], i) for i in range(n) if colors[i] != first[0])

        # Then, find the index and colour of the two last different coloured houses
        last = (colors[n - 1], n - 1)
        second_last = next((colors[i], i) for i in reversed(range(n)) if colors[i] != last[0])

        # If the first and last element has different colours, they are furthest apart
        if first[0] != last[0]:
            return last[1] - first[1]

        # Otherwise, compute remaining distances and return the maximum
        distance1 = second_last[1] - first[1]
        distance2 = last[1] - second[1] if second[0] != last[0] else second_last[1] - second[1]
        return max(distance1, distance2)
