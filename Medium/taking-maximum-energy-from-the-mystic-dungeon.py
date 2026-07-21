# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # Using prefix sum
        n = len(energy)

        # Iterate over every possible end point
        maximum = -inf
        for i in range(n - k, n):
            # Jump backwards through the sequence of magicians
            absorbed = 0
            while i >= 0:
                # Absorbing each magician's enery
                absorbed += energy[i]

                # And store the maximum absorbed energy at any time
                maximum = max(absorbed, maximum)

                # While teleporting k steps back each time
                i -= k
        
        # Finally, return this maximum possible energy from any starting point
        return maximum
