# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # Using deduction
        n = len(nums)

        # If we only have 1 subarray
        if k == n:
            # The result is the maximum
            return max(nums)
        
        # If we instead have n subarrays
        if k == 1:
            # Then count every element appearing at least twice
            seen, twice = set(), set()
            for num in nums:
                if num in seen:
                    twice.add(num)
                seen.add(num)
            
            # The result is the maximum element not appearing twice
            return max(seen - twice, default=-1)
        
        # Otherwise, store the edges as potential missing integers
        candidates = [nums[0], nums[-1]]

        # If these candidates are identical, they are not almost missing
        if candidates[0] == candidates[1]:
            return -1

        # Otherwise, iterate all inner indices
        for i in range(1, n - 1):
            if not candidates:
                break
            
            # If any candidate appear, remove them as candidates
            if nums[i] in candidates:
                candidates.remove(nums[i])
        
        # Then finally, return the largest almost missing integer if it still exists
        return max(candidates, default=-1)


# There are two values of k in which all numbers lay in exactly one k-sized subarray.
# k = n: The whole array only has 1 subarray. Thus all elements can only be in this.
# k = 1: Every element is its own subarray. They only exist in their own.

# In the first case, the largest missing is the maximum of the array.
# In the second case, the largest missing is the maximum element not appearing
# twice in the array.

# In all other cases of k, every element except the two ends, lay in at least 2.
# Thus, in all other cases, we only need to check these edges, returning the maximum,
# that does not appear in any "inner" index. This is because, if it appears in such an
# inner index, then it would also be one of the elements apart of several subarrays.