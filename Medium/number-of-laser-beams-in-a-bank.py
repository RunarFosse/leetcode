# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # For each row, count devices, and store information
        # to iteratively calculate result in one pass
        lasers = 0
        devices_last = 0
        for row in bank:
            devices_current = sum(int(c) for c in row)
            if devices_current == 0:
                continue
            
            lasers += devices_last * devices_current
            devices_last = devices_current
        
        return lasers

        
# First count number of devices on each row.
# Then count lasers between them, this is obvsiously equal to
# devices_r1 * devices_r2, for different rows r_1, r_2 satisfying conditions.