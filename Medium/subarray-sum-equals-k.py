# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = count = 0
        sums = defaultdict(lambda: 0)
        for n in nums:
            sum += n
            count += sums[sum - k]
            sums[sum] += 1
        
        # We never check for exact sum of k, so add counts here
        count += sums[k]
        return count

# As we have negative numbers, sliding window doesnt work.
# We note that if at index i we have sum == a, and at index j we have sum == b.
# If b - k == a, then a - b == k, i.e. sum between numbers i to j equal to k.
# Therefore, if we continuously store sum counts and check if current sum - k
# has happened, then we will find all subarrays whom sum to k.