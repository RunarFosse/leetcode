# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Store forces of dominoes falling on each brick
        n = len(dominoes)
        forces = [0] * n

        # Compute domino forces from bricks falling rightwards
        force = 0
        for i in range(n):
            if dominoes[i] == "R":
                force = n
            elif dominoes[i] == "L":
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
        
        # Subtract the forces from bricks falling leftwards,
        # and replace with final orientation for each brick
        force = 0
        for i in reversed(range(n)):
            if dominoes[i] == "L":
                force = n
            elif dominoes[i] == "R":
                force = 0
            else:
                force = max(force - 1, 0)
            
            if force < forces[i]:
                forces[i] = "R"
            elif force > forces[i]:
                forces[i] = "L"
            else:
                forces[i] = "."
            
        # Finally, return the final orientation of each brick
        return "".join(forces)