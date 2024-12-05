# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Using two pointers
        n = len(start)

        # Iterate both strings
        p1, p2 = 0, 0
        while p1 < n or p2 < n:
            # Skip any underscores in start
            while p1 < n and start[p1] == "_":
                p1 += 1
            
            # Skip any underscores in target
            while p2 < n and target[p2] == "_":
                p2 += 1

            # If either string is finished iterating, break out of loop
            if p1 == n or p2 == n:
                break 
            
            # If not, verify that the two letters match
            if start[p1] == "R":
                # If start is R, check that target is also R, and is more right
                if target[p2] != "R" or p2 < p1:
                    return False
            else:
                # If start is L, check that target is also L, and is more left
                if target[p2] != "L" or p2 > p1:
                    return False
            
            # And increment pointers
            p1 += 1
            p2 += 1

        # The strings match if and only if both are strings are exhausted
        return p1 == p2


# The two strings match if we can move pieces to make them equivalent.
# There are three observations:
# Ls can only move left, Rs can only move right.
# Underscores can be moved over as pleased.
# Ls block Rs from moving right, Rs block Ls from moving left.