# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # Using sliding window
        n = len(nums)

        # Iterate the array
        for i in range(n):
            # Sliding a window of size 4 over it
            for j in range(i + 1, min(i + 4, n)):
                # If there exists a duplicate, we have our repeated element
                if nums[i] == nums[j]:
                    return nums[i]

# The array contains 2N elements, with N+1 elements, and one element appearing N times.
# In other words, the element that is repeated N times is the only one that is
# repeated at all in the array! Thus, we can find this repeated element.

# To ensure that we efficiently find the repeated element in the array, focus on
# the minimal distance between any two duplicate elements. Let's call this minimal
# distance k.

# This would mean that there exist at least k(N - 1) elements in the array
# not equal to the repeated one!

# We have the inequality k(N - 1) <= 2N.
# This holds for 1 and 2, but not for 3! Therefore 3 is the minimal distance between
# any two occurences of the repeated element. This makes it sufficient to slide a
# window of size 3 over the array, checking for duplicates.