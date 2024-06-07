# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    mod = int(1e9) + 7
    def checkRecord(self, n: int) -> int:
        # Using dynamic programming

        # Store dp array where first index declares max number of days absent,
        # and second index maximum number of consecutive days late
        opt = [[1] * 3 for _ in range(2)]
        
        # Then iterate over each day, using previous days dp
        # to compute current days students eligible for award
        for _ in range(n):
            current = [[0] * 3 for _ in range(2)]
            for absent in range(2):
                for late in range(3):
                    # Compute if student is present
                    current[absent][late] = opt[absent][2]

                    # Compute if student is late
                    if late:
                        current[absent][late] += opt[absent][late-1]
                    
                    # Compute if student is absent
                    if absent:
                        current[absent][late] += opt[absent-1][2]
                    
                    # At last, take modulo
                    current[absent][late] %= self.mod
            opt = current

        # Return total eligible students given maximum 2 absents and 3 lates
        return opt[1][2]