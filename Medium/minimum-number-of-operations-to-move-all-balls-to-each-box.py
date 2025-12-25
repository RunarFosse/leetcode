# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Using prefix sum
        n = len(boxes)

        # Compute both directions in one pass
        moves, ballsLeft, ballsRight, movesLeft, movesRight = [0] * n, 0, 0, 0, 0
        for i in range(n):
            # Count balls from the left, as well as the moves to move them
            moves[i] += movesLeft
            ballsLeft += int(boxes[i])
            movesLeft += ballsLeft

            # Do the same with balls from the right
            moves[n - i - 1] += movesRight
            ballsRight += int(boxes[n - i - 1])
            movesRight += ballsRight
        
        # Finally, return the moves to move each ball into each box
        return moves
