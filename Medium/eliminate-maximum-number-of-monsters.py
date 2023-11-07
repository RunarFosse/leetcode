# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Using prefix sum
        n = len(dist)
        arrivals = [0] * n
        for d, s in zip(dist, speed):
            arrival = ceil(d / s)

            if arrival < n:
                arrivals[arrival] += 1
        
        killed = 0
        for i, monsters in enumerate(arrivals):
            killed += monsters
        
            if killed > i:
                return i
        
        return n

# Using prefix sum we can calculate the arrival time of the monsters, and storing
# how many arrive at timestep i in the array arrivals[i].
# We know we maximally can kill n monsters, thus if arrival time > n we can disregard
# them, knowing we are guaranteed to kill them (if they were the current closest monster)

# Iterating through this array we store amount killed, until we reach an index i where 
# amount killed + arrivals[i] >= i. This means they have reached the city, and we are dead.