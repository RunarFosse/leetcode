# Author: Runar Fosse
# Time complexity: O(nk)
# Space complexity: O(k)

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # Using dynamic programming
        subarrays, opt = [0] * k, [0] * k

        # Iterate every value
        for num in reversed(nums):
            temp = [0] * k

            # Increment the current value modulo k's subarray
            temp[num % k] += 1
        
            # And iterate all other remainders
            for r in range(k):
                # Adding the current number to their subarray
                temp[(r * num) % k] += opt[r]
            
            # Override the dp array
            opt = temp

            # And add all current subarrays to count of all total subarrays
            for r in range(k):
                subarrays[r] += opt[r]
        
        # Finally, return the count of all subarrays with each x-value
        return subarrays


# opt(i, r) - The number of subarrays starting from index i whose product divided by k
#             results in a remainder r

# Base case:
# opt(n, _) = 0

# Recurrency;
# opt(i, r) = (if nums[i] % k == 0 then 1 else 0) + opt(i + 1, (r * nums[i]) % k)

# No. states = n * k
# Time complexity per state -> O(1)
# Total time complexity => O(nk)

# By using bottom-up iterative dynamic programming we can reduce the
# total space complexity to O(k)!