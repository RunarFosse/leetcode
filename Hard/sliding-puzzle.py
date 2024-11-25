# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

# As the board is stricly 2x3, this is O(1). Otherwise, both would be
# O((mn)!mn) and O((mn)!) respectively.

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Using BFS

        # Turn board into a tuple of tuples
        board = tuple(tuple(row) for row in board)

        # And perform BFS
        queue, seen = deque([(board, 0)]), set()
        while queue:
            puzzle, steps = queue.popleft()
            if puzzle == ((1,2,3),(4,5,0)):
                return steps

            # Check if the puzzle has been seen before
            if puzzle in seen:
                continue
            seen.add(puzzle)

            # Turn the puzzle into an array, and find the position of 0
            board, position = [[0] * 3 for _ in range(2)], None
            for i, row in enumerate(puzzle):
                for j, cell in enumerate(row):
                    board[i][j] = cell
                    if not cell:
                        position = (i, j)

            # Add all neighbour boards to the queue
            for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                swap = (position[0] + move[0], position[1] + move[1])
                if swap[0] < 0 or swap[0] >= 2 or swap[1] < 0 or swap[1] >= 3:
                    continue
                
                # Perform a move, and add to queue
                board[position[0]][position[1]], board[swap[0]][swap[1]] = board[swap[0]][swap[1]], board[position[0]][position[1]]
                queue.append((tuple(tuple(row) for row in board), steps + 1))
                board[position[0]][position[1]], board[swap[0]][swap[1]] = board[swap[0]][swap[1]], board[position[0]][position[1]]

        # If loop terminates, board cannot be solved
        return -1

# By representing the solution space as a graph, we can BFS from a given
# start position into all neighbour game board states. If the solved state
# lies within this solution space, the game is solvable given the number
# of steps found using BFS.