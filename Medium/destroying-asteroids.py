# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Using greedy

        # Sort the asteroids in ascending order of mass
        asteroids.sort()

        # Then, iterate the asteroids
        for asteroid in asteroids: 
            # If our planet's mass is smaller than the asteroid
            if mass < asteroid:
                # We are destroyed
                return False
            
            # Otherwise, absorb it
            mass += asteroid
        
        # If we absorb all asteroids, we are not destroyed
        return True
