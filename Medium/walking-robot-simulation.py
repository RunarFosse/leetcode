# Author: Runar Fosse
# Time complexity: O(n + m)
# Space complexity: O(n)

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Store each obstacle in a set
        obstacles = set(map(tuple, obstacles))

        # Declare helper functions for use in simulation
        move = lambda pos, dir: (pos[0] + dir[0], pos[1] + dir[1])
        distance = lambda pos: pow(pos[0], 2) + pow(pos[1], 2)

        # Simulate the robot, keeping track of maximum distance from origin
        position, direction = (0, 0), (0, 1)
        max_distance = 0
        for command in commands:
            # If command is less than 0, change direction
            if command < 0:
                if command == -2:
                    direction = (-direction[1], direction[0])
                else:
                    direction = (direction[1], -direction[0])
                continue
            
            # If not, move forward the given units, stopping
            # the robot if it ever hits an obstacle
            for _ in range(command):
                new_position = move(position, direction)
                if new_position in obstacles:
                    break
                position = new_position
            
            # And store maximum distance from the origin
            max_distance = max(distance(position), max_distance)
        
        # Return this maximum distance
        return max_distance