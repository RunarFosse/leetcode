# Author: Runar Fosse
# Time complexity: O(mnk)
# Space complexity: O(mn)

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        opt = [[] for _ in range(n)]

        for i in range(n):
            for t in range(target):
                # Base case
                if i == 0:
                    opt[i].append(1 if t < k else 0)
                    continue
                
                # Recurrency
                opt[i].append(sum(opt[i-1][t - roll] for roll in range(1, min(k+1, t-i+2))))
                
        return opt[n - 1][target - 1] % int(1e9 + 7)

# opt(n, k, t) - Number of different ways of rolling t, given n k-faced die rolls

# Base case:
# opt(1, k, t) = 1 if t <= k else 0
# opt(n, k, t <= 0) = 0

# Recurrency:
# opt(n, k, t) = sum(opt(n-1, k, t-k') for k' in range(1, k+1))

# Number of states -> m*n (where m = target), runtime per state -> O(k).
# Thus giving time complexity of O(mnk).