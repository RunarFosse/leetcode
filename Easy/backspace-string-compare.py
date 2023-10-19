# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        skips = skipt = 0
        ixs, ixt = len(s) - 1, len(t) - 1
        while True:
            skippeds = skippedt = True

            if ixs >= 0:
                if s[ixs] == "#":
                    skips += 1
                    ixs -= 1
                elif skips > 0:
                    skips -= 1
                    ixs -= 1
                else:
                    skippeds = False

            if ixt >= 0:
                if t[ixt] == "#":
                    skipt += 1
                    ixt -= 1
                elif skipt > 0:
                    skipt -= 1
                    ixt -= 1
                else:
                    skippedt = False
        
            # If neither were skipped
            if not (skippeds or skippedt):
                if s[ixs] == t[ixt]:
                    ixs -= 1
                    ixt -= 1
                else:
                    return False
            # Check if one wasn't skipped whilst the other was finished
            # i.e. check if not (one was skipped or the other wasn't finished)
            elif not (skippedt or ixs >= 0) or not (skippeds or ixt >= 0):
                return False
            
            # If both are finished
            if ixs == -1 and ixt == -1:
                return True
