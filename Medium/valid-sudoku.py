# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(n)]
        subboxes = [set() for _ in range(n)]

        # Add each num to each set
        for y in range(n):
            for x in range(n):
                num = board[y][x]
                if num == ".": # . means no number
                    continue
                # z is subbox index
                z = (x // 3) + (y // 3) * 3

                # If there are any intersections, board is invalid
                row_invalid = rows[y].issuperset({num})
                column_invalid = columns[x].issuperset({num})
                subbox_invalid = subboxes[z].issuperset({num})
                if row_invalid or column_invalid or subbox_invalid:
                    return False

                rows[y].add(num)
                columns[x].add(num)
                subboxes[z].add(num)
        
        return True