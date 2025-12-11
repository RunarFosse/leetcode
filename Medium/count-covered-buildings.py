# Author: Runar Fosse
# Time complexity: O(m)
# Space complexity: O(m)

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Using greedy
        
        # Store the min/max x position at each y, min/max y position at each x
        xs, ys = defaultdict(lambda: (n, 0)), defaultdict(lambda: (n, 0))
        for x, y in buildings:
            xs[y] = (min(x, xs[y][0]), max(x, xs[y][1]))
            ys[x] = (min(y, ys[x][0]), max(y, ys[x][1]))

        # Then, iterate all buildings again
        covered = 0
        for x, y in buildings:
            # And check if the current value is a minimum or maximum
            left = xs[y][0] < x
            right = xs[y][1] > x
            under = ys[x][0] < y
            over = ys[x][1] > y
            if left and right and under and over:
                covered += 1
        
        # Finally, return the number of covered buildings
        return covered
