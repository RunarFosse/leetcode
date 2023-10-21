# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(k)

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # Using dynamic programming
        maximums = deque()
        for i in range(len(nums)):
            if maximums:
                nums[i] += nums[maximums[0]]
                if maximums[0] <= i-k:
                    maximums.popleft()

            while maximums and nums[maximums[-1]] < nums[i]:
                maximums.pop()
            
            if nums[i] > 0:
                maximums.append(i)
        
        return max(nums)


# We know that the subsequence has to be psuedo-continuous, up to k-indices.
# Therefore, for each index i we calculate the maximum value from picking 
# i (nums[i]), and finding what other number (if any) we should add 
# from the k previous (max(0, opt[i-1], opt[i-2], ..., opt[i-k])).

# To optimize runtime we can use a double ended queue for opt[i-1], ..., opt[i-k],
# continuously updating and storing the max value, (in total O(n) time!).

# Note: Instead of using seperate opt[] array, we override nums[] array
# making space complexity way lower (this is possible as we only iterate
# nums[] once, and only look backwards into the "modified" nums[] (i.e. opt))

# opt[i] - Maximum prefix subsequence sum for indicies less than or equal to i.

# Base case:
# opt[0] = nums[0]      - Subsequence can't be empty

# Recurrency:
# opt[i] = nums[i] + max(0, opt[i-1], opt[i-2], ..., opt[i-k])