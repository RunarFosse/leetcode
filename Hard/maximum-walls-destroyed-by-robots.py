# Author: Runar Fosse
# Time complexity: O((m log m + nlog n)
# Space complexity: O(m + n)

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # Using dynamic programming
        m, n = len(walls), len(robots)

        # First, sort the robots and walls in ascending order
        indices = sorted(range(n), key=lambda i: robots[i])
        robots, distance = [robots[i] for i in indices], [distance[i] for i in indices]
        walls.sort()

        # Keep a sliding window of walls that can be destroyed by each robot
        left_interval, right_interval = [m, m], [m, m]
        next_left_wall = None
        
        # Iterate every robot
        opt = [0, 0]
        for i in reversed(range(n)):
            position, reach = robots[i], distance[i]

            # First, compute the current robot's left and right boundary
            left, right = position - reach, position + reach
            if i > 0:
                left = max(robots[i - 1] + 1, left)
            if i < n - 1:
                right = min(robots[i + 1] - 1, right)
            
            # Then, slide windows and compute wall intervals it can destroy
            while left_interval[0] and walls[left_interval[0] - 1] >= left:
                left_interval[0] -= 1
            while left_interval[1] and walls[left_interval[1] - 1] > position:
                left_interval[1] -= 1
            while right_interval[0] and walls[right_interval[0] - 1] >= position:
                right_interval[0] -= 1
            while right_interval[1] and walls[right_interval[1] - 1] > right:
                right_interval[1] -= 1   

            # And compute how many walls it can destroy by shooting left, or right
            left_destroyed = left_interval[1] - left_interval[0]
            right_destroyed = right_interval[1] - right_interval[0]

            # If we are not the last robot, we need to compute a destruction overlap
            overlap = 0
            if next_left_wall is not None:
                overlap = max(right_interval[1] - next_left_wall, 0)
            
            # Finally, for each shooting direction, compute maximum destruction
            opt = [
                left_destroyed + max(opt), 
                right_destroyed + max(opt[0] - overlap, opt[1])
            ]

            # And store current left wall boundary for the next iteration
            next_left_wall = left_interval[0]

        # At last, return the maximum destruction done by all robots
        return max(opt)


# opt(i, dir) - The number of walls destoryed by robots at and after index i,
#               if robot i shoots either left (0), or right (1), given by dir.

# Base case:
# opt(n, _) = 0

# Recurrency:
# opt(i, dir) | dir == 0 = left_destroyed + max(opt(i + 1, 0), opt(i + 1, 1))
#             | dir == 1 = right_destroyed + max(opt(i + 1, 0) - overlap, opt(i + 1, 1))
#   where left = max(robots[i] - distance[i], robots[i - 1] + 1)
#         right = min(robots[i] + distance[i], robots[i + 1] - 1)
#         next_left = max(robots[i + 1] - distance[i + 1], robots[i] + 1)
#         left_wall = bisect_left(walls, left)
#         middle_wall_left = bisect_right(walls, robots[i])
#         middle_wall_right = bisect_left(walls, robots[i])
#         right_wall = bisect_right(walls, right)
#         next_left_wall = bisect_left(walls, next_left)
#         left_destroyed = middle_wall_left - left_wall
#         right_destroyed = right_wall - middle_wall_right
#         overlap = max(right_wall - next_left_wall, 0)

# No. states = 2 * n
# Time complexity per state -> O(log m)
# Total time complexity => O(nlog m)

# By iterating each robot iteratively using bottom-up dynamic programming,
# we can reduce the space complexity to O(1).

# Also, instead of using binary search to find left and right walls, we can
# use a two pointer approach over each iteration, reducing time per state to O(1).
# This in turn lowers time complexity even further to O(m + n).

# All this however assumes both robots and walls are sorted by distance, 
# which would dominate time complexity to O(mlog m + nlog n).
# Same for the space complexity, dominated by O(m + n)