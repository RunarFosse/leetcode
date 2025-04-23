# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Iterate every number
        groups = defaultdict(int)
        for i in range(1, n + 1):
            # Count its digit sum
            digits = 0
            while i:
                digits += i % 10
                i //= 10
            
            # And add to group
            groups[digits] += 1
        
        # Then, count groups of the largest size
        size, count = 0, 0
        for group in groups.values():
            if group == size:
                count += 1
            elif group > size:
                size = group
                count = 1
        
        # Finally, return count of the largest groups
        return count