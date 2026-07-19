# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Using binary search
        n = len(nums)

        # Iterate the array, computing longest increasing subsequences left-to-right
        LIS, increasing = [0] * n, []
        for i in range(n):
            # By binary searching the bucket with the largest entry less than num
            index = bisect_left(increasing, nums[i], key=lambda l: l[-1])

            # If there is such a patience pile, add to it
            if index < len(increasing):
                increasing[index].append(nums[i])
            else:
                # If not, start a new pile
                increasing.append([nums[i]])
            
            # And count current longest increasing subsequence at this element
            LIS[i] = index + 1
        
        # Then iterate again, computing longest decreasing subsequence right-to-left
        LDS, decreasing = [0] * n, []
        for i in reversed(range(n)):
            # By binary searching the bucket with the smallest entry larger than num
            index = bisect_left(decreasing, nums[i], key=lambda l: l[-1])

            # If there is such a patience pile, add to it
            if index < len(decreasing):
                decreasing[index].append(nums[i])
            else:
                # If not, start a new pile
                decreasing.append([nums[i]])
            
            # And count current longest decreasing subsequence at this element
            LDS[i] = index + 1
        
        # Finally, iterate every index again
        mountain = 0
        for i in range(n):
            # If this index is a valid peak candidate
            if LIS[i] > 1 and LDS[i] > 1:
                # Compute current mountain size as sum of both, decremented
                # by one to account for current index's double entry
                mountain = max(LIS[i] + LDS[i] - 1, mountain)

        # And remove all elements not a part of the maximum mountain
        return n - mountain


# To create a mountain array, we must remove all local peaks.
# A mountain array is only valid if there exists a single maximum: the global maximum.

# To find how many removals need to be done to make this mountain array, we can
# use longest increasing and decreasing subsequence values occuring before and after
# each index, respectively. We can then "remove" the values disrupting the union of 
# these LIS and LDS sequences from containing every index.
# Those can again be computed efficiently by using patience piles.

# A patience pile stores LIS by index in buckets. The tail of every bucket before
# an element's bucket are values which are smaller, and which occur before in the array.
# In this way, we can efficiently compute the LIS ending at each index,
# by checking which patience pile they should be added into.

# Take these LIS buckets:
# [[0], [4, 3], [6, 6, 5]]
#
# These has the bucket tails:
# [0, 3, 5]
#
# Adding a 1 now adds to the first bucket tail with a value greated than or equal, i.e.
# [[0], [4, 3, 1], [6, 6, 5]]
# 
# As the 1 was placed in the second bucket, then:
# The LIS ending at this 1 is of length 2.