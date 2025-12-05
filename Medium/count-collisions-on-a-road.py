# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countCollisions(self, directions: str) -> int:
        # First count total cars
        collisions = len(directions)

        # Then, remove edge cars which do not collide
        for direction in directions:
            if direction != "L":
                break
            collisions -= 1
        for direction in reversed(directions):
            if direction != "R":
                break
            collisions -= 1
        
        # Then, remove all stationary cars, and return collisions
        collisions -= directions.count("S")
        return collisions


# Observation: 
# 
# - Cars that collide turn stationary
# -> Cars can only collide with one car each
# -> R S L == R L
# -> R R S L L == R R L L
# -> Stationary cars do not collide
#
# And, left cars on the left, right cars on the right, do not collide with anyone