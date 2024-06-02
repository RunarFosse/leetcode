# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0

        pointer = len(s)-1
        # First remove all trailing 0s
        while pointer > 0 and s[pointer] == "0":
            steps += 1
            pointer -= 1
        
        # If we are not finished, then we need to start adding
        if pointer > 0:
            steps += 2
        
        # At last, add and divide until we reach the end
        while pointer > 0:
            if s[pointer] == "0":
                steps += 1
            steps += 1
            pointer -= 1

        # Return the total number of steps
        return steps
        

# Division by 2 is equal to right shifting bit string once
# Adding 1 is equal to setting all right-most 1s to 0,
# as well as the right-most 0 to 1.