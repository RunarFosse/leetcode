# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Using dynamic programming
        n = len(arr)

        # First, add every element and their index to a dictionary
        elements = {arr[i]: i for i in range(n)}

        # Then, compute the length of every longest fibbonacci subsequence
        maximum = 0
        opt = [[0] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in reversed(range(i + 1, n)):
                element = arr[i] + arr[j]
                if element not in elements:
                    continue
                
                k = elements[element]
                opt[i][j] = 1 + opt[j][k]

                # Also, store the longest fibonacci sequence seen
                maximum = max(opt[i][j], maximum)
    
        # Finally, return this longest fibonacci sequence seen
        return maximum + (2 if maximum else 0)


# opt(i, j) - The length of the longest fibonacci subsequence starting
#             at the indices i and j

# Base case:
# opt(_, n) = 0
# opt(n, _) = 0

# Recurrency:
# opt(i, j) | if arr[i] + arr[j] in elements at k = 1 + opt(j, k)
#           | otherwise                           = 0