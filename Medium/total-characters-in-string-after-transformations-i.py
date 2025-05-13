# Author: Runar Fosse
# Time complexity: O(n + t)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # First, count frequency of each character
        indexOf = lambda c: ord(c) - ord("a")
        frequencies = [0] * 26
        for c in s:
            frequencies[indexOf(c)] += 1

        # Turn frequency array into deque for optimal simulation
        frequencies = deque(frequencies)
        
        # Then, iteratively apply all transformations
        for _ in range(t):
            # Transform all characters one to the right
            zs = frequencies.pop()
            frequencies.appendleft(zs)

            # And add one 'b' for each 'z'
            frequencies[1] = (frequencies[1] + zs) % self.mod
        
        # Finally, return number of characters mod
        return sum(frequencies) % self.mod
