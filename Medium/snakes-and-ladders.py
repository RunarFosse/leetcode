# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Using BFS
        n = len(board)
        
        # Start BFS from the first square
        queue, seen = deque([(1, 0)]), set()
        while queue:
            square, distance = queue.popleft()
            if square in seen:
                continue
            seen.add(square)
            
            # Otherwise, comput the row and column from the given square
            div, rem = divmod(square - 1, n)
            row, column = (n - 1) - div, (n - rem - 1 if div % 2 else rem)

            # If the current square is a snake or ladder, move
            if board[row][column] != -1:
                square = board[row][column]

            # If we've reached the end, return the distance
            if square == pow(n, 2):
                return distance

            # And add all positions reachable from there
            for i in range(square, min(square + 6, pow(n, 2))):
                queue.append((i + 1, distance + 1))
            
        # If the while loop terminates, it is not possible to reach the goal
        return -1
