# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def countPartitions(self, nums: List[int], k: int) -> int:
        # Using dynamic programming
        n = len(nums)

        # Store number of valid partitions and suffixes sum of later partitions
        opt = [0] * n + [1]
        suffixes = [0] * n + [1]

        # Also store a max-min monotonic queue of values
        end, maximums, minimums = n, deque([]), deque([])
        for start in reversed(range(n)):
            # Maintain the maximum and minimum monotonic queues
            while maximums and nums[maximums[-1]] <= nums[start]:
                maximums.pop()
            maximums.append(start)
            while minimums and nums[minimums[-1]] >= nums[start]:
                minimums.pop()
            minimums.append(start)
        
            # Then, expand the window with new values until difference is less than k
            while maximums and minimums and nums[maximums[0]] - nums[minimums[0]] > k:
                # Remove any element outside the window
                if maximums[0] == end - 1:
                    maximums.popleft()
                if minimums[0] == end - 1:
                    minimums.popleft()
                
                # And shrink it
                end -= 1
            
            # If we are still in the last possible partition
            if end == n:
                # We can compute optimal directly
                opt[start] = suffixes[start + 1] % self.mod
            else:
                # Otherwise, compute as difference of suffixeses
                opt[start] = (suffixes[start + 1] - suffixes[end + 1]) % self.mod
            
            # And update suffix sum
            suffixes[start] = (opt[start] + suffixes[start + 1]) % self.mod
        
        # Finally, return the total number of partitions with at most inner difference k
        return opt[0]

# opt(i) - The number of valid partitions including and after index i.

# Base case:
# opt(n) = 1

# Recurrency:
# opt(i) = sum(opt(j), j <- [i+1..n], max(nums[i+1..j]) - min(nums[i+1..j]) <= k)

# Using suffix sums we can reduce the time complexity of the recurrency:
# opt(i) = suffixes[j] - suffixes[i]
#          where j = next(l, l <- [i+1..n], max(nums[i+1..j]) - min(nums[i+1..j]) <= k)

# Here, the suffixes hold sum of all following opt values:
# suffixes[i] = sum(opt(j), j <- [i+1..n])

# Using bottom-up dynamic programming and min-max monotonic queue we can optimize
# the time and space complexity to O(n)!