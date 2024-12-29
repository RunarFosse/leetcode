class Solution:
    def minimumSteps(self, s: str) -> int:
        # Store current number of steps, and how many black balls we've seen
        steps, blacks = 0, 0

        # Iterate the string
        for c in s:
            # If the ball is white, "bubble" all black
            # balls we've seen 1 step to the right
            if c == "0":
                steps += blacks

            # Otherwise, increment number of black balls
            else:
                blacks += 1
        
        # Finally, return the number of steps to group blacks to the right
        return steps
    
    