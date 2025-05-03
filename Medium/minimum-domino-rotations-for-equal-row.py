# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        self.tops, self.bottoms = tops, bottoms

        # For each of the possible numbers, count domino rotations
        rotations_1 = self.countRotations(tops[0])
        rotations_2 = self.countRotations(bottoms[0])

        # Then, return the minimum number of rotations
        if rotations_1 != -1 and rotations_2 != -1:
            return min(rotations_1, rotations_2)
        return rotations_1 if rotations_2 == -1 else rotations_2
        
    def countRotations(self, num: int) -> int:
        # Given the number, count top and bottom rotations
        top_rotations, bottom_rotations = 0, 0

        for top, bottom in zip(self.tops, self.bottoms):
            # If neither is equal to the number, we cannot rotate
            if top != num and bottom != num:
                return -1
            
            # Otherwise, count
            if top != num:
                top_rotations += 1
            if bottom != num:
                bottom_rotations += 1
        
        # Finally, return the minimum between them
        return min(top_rotations, bottom_rotations)


# To make a row of equal dominoes we only have two possibilities: the two
# cases of the first domino, tops[0] and bottoms[0].