# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # First split and map all versions to integers
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))

        # Then iterate over versions and compare
        n, m = len(version1), len(version2)
        for i in range(max(n, m)):
            current1 = version1[i] if i < n else 0
            current2 = version2[i] if i < m else 0

            if current1 < current2:
                return -1
            if current1 > current2:
                return 1
        
        # If the two versions are equal, return 0
        return 0
