# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Iterate the numbers
        maximums, minimums = (-inf, -inf, -inf), (inf, inf)
        for num in nums:
            # Store the three largest elements of the array
            if num > maximums[0]:
                maximums = (num, maximums[0], maximums[1])
            elif num > maximums[1]:
                maximums = (maximums[0], num, maximums[1])
            elif num > maximums[2]:
                maximums = (maximums[0], maximums[1], num)
            
            # And the two smallest elements of the array
            if num < minimums[0]:
                minimums = (num, minimums[0])
            elif num < minimums[1]:
                minimums = (minimums[0], num)
        
        # Finally, compute the maximum product with these factors
        return max(prod(maximums), maximums[0] * prod(minimums))


# To maximize the product of three numbers, we need to maximize the equation:
# a * b * c

# WLOG c is positive -> and the maximum element of the array.
# Then we need to find the two numbers a and b that maximize a * b.

# For that to be the case, either:
# a and b are both positive.
# a and b are both negative.

# For the positive case, c is already the maximum element of the array.
# Then a and b each have to be the second and third maximum element, respectively.

# For the negative case, a and b have to be the minimum and second minimum element,
# respectively.