# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    mod = int(1e9) + 7
    def knightDialer(self, n: int) -> int:
        C, V, H, Z = 4, 2, 2, 1
        for _ in range(n - 1):
            C, V, H, Z = (2*V + 2*H), C, (2*Z + C), H
        
        solution = C + V + H + Z + (1 if n == 1 else 0)
        return solution % self.mod


# We have that:
# 1 -> 6, 8
# 2 -> 7, 9
# 3 -> 4, 8
# 4 -> 3, 9, 0
# 5 ->
# 6 -> 1, 7, 0
# 7 -> 2, 6
# 8 -> 1, 3
# 9 -> 4, 2
# 0 -> 4, 6

# Out of these we have 4 different groups. Corners, horizontal sides, vertical sides and 0.
# Note, 5 isnt included, as it doesn't reach anywhere.

# Corners reach both the vertical and horizontal sides.
# Vertical sides reach the corners.
# Horizontal sides reach the corners and 0.
# 0 reach the horizontal sides.

# Corners has 4 members
# Vertical has 2
# Horizontal has 2
# 0 has 1

# We can use this to create a arithmetic series, solving the problem mathematically.