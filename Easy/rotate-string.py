# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If they are not equal in length, goal is not a rotation of s
        n = len(s)
        if len(goal) != n:
            return False

        # Iterate the goal string
        for i in range(n):
            # Iterate from this index to see if it creates the string s
            pointer = 0
            while pointer < n and goal[i] == s[pointer]:
                i = (i + 1) % n
                pointer += 1

            # If so, goal is a rotation of s
            if pointer == n:
                return True
        return False