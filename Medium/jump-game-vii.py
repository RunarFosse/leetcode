# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Using sliding window
        n = len(s)

        # First, check if the last element is not equal to '0'
        if s[n - 1] != "0":
            # If so, we cannot jump to it
            return False
        
        # Otherwise, start at the initial object
        reachables = 0
        reachable = [True] + [False] * (n - 1)
        for i in range(1, n):
            # First, check the last index to jump to here
            if i >= minJump and reachable[i - minJump]:
                # If that is reachable, we have one more reachable source
                reachables += 1
            
            # Then, check the element that just went out of reach
            if i > maxJump and reachable[i - maxJump - 1]:
                # If that was reachable, we have one less reachable source
                reachables -= 1
            
            # Finally, this element is reachable if it is '0' and has a reachable source
            reachable[i] = s[i] == "0" and reachables > 0
        
        # Finally, return if the last element is reachable
        return reachable[-1]
