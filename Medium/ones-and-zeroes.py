# Author: Runar Fosse
# Time complexity: O(mnk)
# Space complexity: O(mn)

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Using dynamic programming
        opt = [[0] * (n + 1) for _ in range(m + 1)]
        for string in strs:
            # Compute the number of ones and zeros in the string
            ones = sum(map(lambda c: int(c), string))
            zeros = len(string) - ones

            # And add to feasible subsets
            for i in reversed(range(zeros, m + 1)):
                for j in reversed(range(ones, n + 1)):
                    opt[i][j] = max(1 + opt[i - zeros][j - ones], opt[i][j])
        
        # Finally, return the largest subset containing at most m 0's and n 1's
        return opt[m][n]
    
# opt(m, n) is the largest subset of strs, containing at most m 0's and n 1's

# N.o. states = mn
# Runtime per state = O(k)
# => Time complexity of O(mnk)