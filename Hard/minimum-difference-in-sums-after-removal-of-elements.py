# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # Using greedy
        n = len(nums) // 3

        # First, minimize sum_first
        max_heap = [-nums[i] for i in range(n)]
        heapify(max_heap)
        sum_firsts = [-sum(max_heap)]
        for i in range(n, 2*n):
            # Add the next element
            heappush(max_heap, -nums[i])
            current = nums[i]

            # Remove previous last element
            current -= -heappop(max_heap)
            sum_firsts.append(sum_firsts[-1] + current)
        
        # Then, maximize sum_second
        min_heap = nums[2*n:]
        heapify(min_heap)
        sum_second = sum(min_heap)
        difference = sum_firsts[-1] - sum_second
        for i in reversed(range(n, 2*n)):
            # Add the next element
            heappush(min_heap, nums[i])
            sum_second += nums[i]

            # Remove previous last element
            sum_second -= heappop(min_heap)

            # And store current minimum difference
            difference = min(sum_firsts[i - n] - sum_second, difference)
        
        # Finally, return the minimum difference
        return difference

        
# To minimize the differences between sum_first and sum_second
# we could equivalently try to minimize sum_first, and maximize sum_second.

# We can construct sum_first with n elements from the left and sum_second
# with n elements from the right.

# To minimize sum_first, we iterate from the left, summing n numbers, and
# storing said sum in an array, where array[i] is the minimum sum up until index i.
# To minimize said sum, we easily keep every element in a max heap.

# The opposite can be done for sum_second, iterating from the right, summing n numbers,
# and keeping a min heap, popping the smallest number and maximizing the sum.