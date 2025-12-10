# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        # Count the number of permutations of the array
        permutations = 1
        for i in range(1, n):
            permutations = (permutations * i) % self.mod

            # However, return zero if it's impossible to unlock every computer
            if complexity[i] <= complexity[0]:
                return 0

        # Otherwise, return this number of permutations
        return permutations
