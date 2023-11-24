# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Using greedy
        full_children = 0
        g.sort()
        s.sort()

        gp, sp = len(g), len(s)
        while gp and sp:
            # If you can give the largest cookie to a child, do it
            if s[sp-1] >= g[gp-1]:
                full_children += 1
                sp -= 1
            gp -= 1
        
        return full_children