# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(m)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cmaps, cmapt = {}, {}
        for i, (cs, ct) in enumerate(zip(s, t)):
            maps, mapt = cmaps.get(cs), cmapt.get(ct)
            if maps == None and mapt == None:
                cmaps[cs] = i
                cmapt[ct] = i
            elif maps != None and mapt != None:
                if maps != mapt:
                    return False
            else:
                return False
        
        return True