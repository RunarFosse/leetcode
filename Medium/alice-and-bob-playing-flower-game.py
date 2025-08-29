# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Compute the solution using half the rectangle's area
        return (m * n) // 2

        
# To guarantee a win for Alice, each lane has to have a different parity of flowers.
# This can be rephrased as when the sum of flowers in both lanes, is odd.
# For all values i in [1, n], this happens for roughly half of the values in [1, m],
# (based on n's parity). Using n and m to construct a rectangle, the number
# of valid solutions is thus equal to the half of that rectangles area!