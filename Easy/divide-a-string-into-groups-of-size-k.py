# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)

        # Iterate the string in groups of k
        groups = []
        for i in range(0, n, k):
            # And add them to the array
            groups.append(s[i:i+k])
        
        # If the last group is too small, pad it with fill
        if len(groups[-1]) != k:
            groups[-1] += fill * (k - len(groups[-1]))

        # Finally, return the groups
        return groups