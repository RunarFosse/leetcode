# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # Using Fenwick tree
        n = len(nums)

        # Compute all prefix sums
        prefixes = list(accumulate(nums, initial=0))

        # Give an index to each unique prefix sum, called coordinate compression
        values = sorted(set(prefixes))
        indices = {value: i for i, value in enumerate(values)}

        # Then, store prefix sum indices in a Fenwick tree (Binary indexed tree)
        bit = Fenwick(len(values))

        # Then, iterate each ending index of a subarray of at least size l
        minimum = inf
        for i in range(l, n + 1):
            # Add the most recent prefix sum to the Fenwick tree
            bit.update(indices[prefixes[i - l]], 1)

            # Remove any prefix sum outside a subarray of size r
            if i > r:
                bit.update(indices[prefixes[i - r - 1]], -1)
            
            # Find the number of prefix sums smaller or equal to the current one
            index = bisect_left(values, prefixes[i])
            count = bit.query(index - 1)

            # If there are any such prefix sums
            if count > 0:
                # Find the largest prefix sum strictly smaller than the current
                largest = values[bit.kth(count)]

                # Using this to store the minimum positive subarray sum
                minimum = min(prefixes[i] - largest, minimum)
            
        # Finally returning this subarray sum for subarrays sized between l and r
        return minimum if minimum < inf else -1


class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i: int, delta: int) -> None:
        # Convert to 1-based indexing
        i += 1
    
        # Iterate the tree downwards
        while i <= self.n:
            # Increasing the value of each step
            self.tree[i] += delta

            # And moving up the tree, by adding the least significant bit
            i += i & (-i)
    
    def query(self, i: int) -> int:
        # Convert to 1-based indexing
        i += 1

        # Iterate the tree upwards
        result = 0
        while i > 0:
            # Accumulating values on the way
            result += self.tree[i]

            # And moving down the tree, by removing the least significant bit
            i -= i & (-i)
        
        return result

    def kth(self, k: int) -> int:
        # Find the 0-based index of the kth element
        i, bit = 0, 1 << (self.n.bit_length() - 1)

        # Iterate blocks of the Fenwick tree
        while bit:
            # If this block does not contain our k'th element
            j = i + bit
            if j <= self.n and self.tree[j] < k:
                # We can skip it, and subtract its frequency
                i = j
                k -= self.tree[j]
            
            # Then halve the block size
            bit >>= 1
        
        # The resulting index is the index of the k'th element
        return i
