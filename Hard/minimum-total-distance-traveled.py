# Author: Runar Fosse
# Time complexity: O(mn + mlog m + nlog n)
# Space complexity: O(m + n)

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Using dynamic programming
        n = len(robot)

        # First, sort the robots and factories in ascending order of position
        robot.sort()
        factory.sort()

        # Then, iterate each of the factories
        opt = [inf] * n + [0]
        for position, limit in reversed(factory):
            # First, compute the distance prefix sum from robots to this factory
            prefixes = [0]
            for i in range(n):
                prefixes.append(abs(robot[i] - position) + prefixes[-1])
            
            # Compute all candidate endpoints, distance when repairing k robots
            endpoints = [prefixes[k] + opt[k] for k in range(n + 1)]

            # And slide a window over each of the robots, and picking the number
            # of robots to repair by choosing current minimizing robot endpoint
            temp = opt.copy()
            queue, end = deque([]), 0
            for i in range(n):
                # Shrink and expand the window until covering all robots within limit
                while queue and queue[0] < i:
                    queue.popleft()
                while end <= min(i + limit, n):
                    # Maintaining a increasing monotonic queue
                    while queue and endpoints[queue[-1]] >= endpoints[end]:
                        queue.pop()
                    queue.append(end)
                    end += 1

                # And repair robots based on the current minimizing endpoint
                temp[i] = endpoints[queue[0]] - prefixes[i]
            opt = temp

        # Finally, return the minimum total distance traveled to repair all robots
        return opt[0]
    

# opt(i, j) - Minimum distance traveled to repair robots at or after index i,
#             by using the factories at or after index j.

# Base case:
# opt(n, m) = 0
# opt(i, m) = inf

# Recurrency:
# opt(i, j) = min(current + opt(i', j + 1) for i' in [0..limit]))
#             where position, limit = factory[j]
#                   current = sum(abs(robot[index] - position) for index in [i..i'])

# No. states = m * n
# Time complexity per state -> O(n)
# Total time complexity => O(mn^2)

# By using distance prefix sum and minimizing monotonic queue,
# total time complexity can be reduced to O(mn)

# Space complexity can be reduced to O(n) by utilizing bottom-up dynamic programming.