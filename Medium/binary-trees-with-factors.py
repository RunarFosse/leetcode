# Author: Runar Fosse
# Time complexity: O(n sqrt(n))
# Space complexity: O(n)

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # Using dynamic programming
        arr.sort()
        mod = 1e9+7

        opt = []
        index = {}
        trees = 0
        for i in range(len(arr)):
            index[arr[i]] = i
            opt.append(1)

            # Find factors of arr[i] in arr
            for j in range(i):
                # No factor of arr[i] can be bigger than sqrt(arr[i])
                if arr[j] > sqrt(arr[i]):
                    break

                k = arr[i] / arr[j]
                if not index.get(k) is None:
                    opt[i] += opt[j] * opt[index[k]]
                    # Double if the factors are distinct
                    if arr[j] != k:
                        opt[i] += opt[j] * opt[index[k]]
            
            trees += opt[i] % mod
        
        return int(trees % mod)

# First sort list in ascending order
# Then, we know that a binary tree can only consist of nodes
# strictly less than the current root.

# opt(i) - number of different binary trees for root i

# Base case:
# opt(0) = 1

# Recurrency:
# opt(i) = 1 + sum(opt(f1)*opt(f2))     * 2   if f1 != f2 (*)
# where f1, f2 are two factors of i in arr

# As we can see, base case is implicit from recurrency given i = 0.

# If we break the "find factors" loop when our numbers are bigger than sqrt(i) 
# we get an amazing speedup, making our runtime sqrt(n) instead of n!
# Now we need to remember to double every opt(f1) * opt(f2) as long as f1 != f2 (*)

# N.o states = n, runtime per state is O(sqrt(n))
# Thus, time complexity of O(n sqrt(n))