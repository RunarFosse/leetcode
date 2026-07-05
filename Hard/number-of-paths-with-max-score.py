# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # Using dynamic programming
        n = len(board)

        # First, compute the maximum score path on the board
        opt = [[-inf, 0] for _ in range(n + 1)]
        for i in reversed(range(n)):
            current = [[0, 1] for _ in range(n)] + [[-inf, 0]]
            for j in reversed(range(n)):
                character = board[i][j]

                # If we are at the start, we have come from nowhere
                if character == "S":
                    continue

                # If we have an obstacle, set score to negative infinity
                if character == "X":
                    current[j] = [-inf, 0]
                    continue

                # Otherwise, compute the maximum score possible by taking each step
                points = int(character) if character.isnumeric() else 0
                nexts = (current[j + 1], opt[j], opt[j + 1])
                score = max(next[0] for next in nexts)
                paths = sum(next[1] for next in nexts if next[0] == score) % self.mod
                current[j] = [score + points, paths]
            opt = current
        
        # If the maximum possible score is negative infinity, there is no path
        maximum = opt[0]
        if maximum[0] == -inf:
            return [0, 0]
        
        # Otherwise, return the maximum score path with its count
        return maximum


# opt(i, j) - Maximum score of path and number of paths with that score from
#             (i, j) to S, i.e. (n - 1, n - 1).

# Base case:
# opt(n - 1, n - 1) = [0, 1]
# opt(n, _) = [-inf, 0]
# opt(_, n) = [-inf, 0]
# opt(i, j) = [-inf, 0]          if board[i][j] == "X"

# Recurrency:
# opt(i, j) = [score + points, paths]
#           where points = int(board[i][j])
#                 nexts = (opt(i, j + 1), opt(i + 1, j), opt(i + 1, j + 1))
#                 score = max(next[0] for next in nexts)
#                 paths = sum(next[1] for next in nexts if next[0] == score) % mod

# N.o. states = n * n
# Time complexity per state -> O(1)
# Final time complexity => O(n^2)

# With space compression, space complexity => O(n)