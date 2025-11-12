# Author: Runar Fosse
# Time complexity: O(n^2log k)
# Space complexity: O(1)

# where k is the maximum number in the array

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Using sliding window
        n = len(nums)

        # First, count the number of ones already in the array
        ones = sum(filter(lambda num: num == 1, nums))

        # If there already exists a one, return early
        if ones:
            return n - ones

        # Slide a window over the array
        start, smallest = 0, 1e9
        for end in range(n):
            # If the window is coprime
            while start <= end and gcd(*nums[start:end + 1]) == 1:
                # Store the smallest possible size, and shrink the window
                smallest = min(end - start + 1, smallest)
                start += 1
        
        # Finally, return the minimum number of operations, if possible
        if smallest > n:
            return -1
        return smallest + n - 2


# We can replace the whole array with 1s if there is at least 2 coprimes in the array.
# Additionally, if there exists a 1 in the array, then it will take n - x operations
# to spread out into the array, given x existing ones.
# If there does not exist a one, we can create one by finding a subarray with
# a gcd of 1, which then will take m - 1 number of operations, with a subarray sized m.