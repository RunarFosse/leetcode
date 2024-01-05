# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(1)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Using binary search
        length = 1
        for i in range(1, len(nums)):
            num = nums[i]
            # If the current number is larger than last subsequence element,
            # then append it to the back
            if num > nums[length-1]:
                nums[length] = num
                length += 1
            # If not, binary search the first element in the subsequence
            # greater or equal to num, and replace that.
            else:
                replace = bisect_left(nums, num, lo=0, hi=length)
                nums[replace] = num

        # Return the final length of our increasing subsequence
        return length

# We store a current "valid" subsequence, and for each number in the nums list we
# either append it to the back if it keeps our subsequence "valid". However if it
# doesn't, we replace the first element in the subsequence which is greater or 
# equal to that number. This will mean our "valid" subsequence no longer represents
# an actual subseqence in the nums list, but instead represents a sort of "what-if"
# subsequence gotten by skipping/picking elements in another order without 
# "forgetting" our previous steps.

# Instead of iterating our current subsequence to find the first number which is
# greater or equal to our current number we can perform binary search instead,
# reducing our time complexity from n^2 to n log n!

# By using the nums list as our current subsequence we can do this in linear space,
# as our current stack element will always be at or behind our index in the nums list.
# We also know that our current length will be equal to the end_index in said list.