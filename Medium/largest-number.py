# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

# Define a custom comparator to do custom comparisons (in Python 3)
class NumberComparator(str):
    def __lt__(n1, n2):
        return n1 + n2 > n2 + n1

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Using greedy
        nums = sorted(map(str, nums), key = NumberComparator)

        # If first digit is zero, then the whole number is zero
        if nums[0] == "0":
            return "0"

        # If not, concatenate nums
        return "".join(nums)
        
# Sort list after if two numbers create a bigger number together:
# [ 3, 30, 34, 5, 9, 98, 99, 89 ] -> [ 9, 99, 98, 89, 5, 34, 3, 30 ]