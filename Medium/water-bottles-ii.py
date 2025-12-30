# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # Using analytic solution
        root = sqrt(numExchange*numExchange - 3*numExchange + 2*numBottles + 9/4)
        x = ceil(3/2 - numExchange + root) - 1
        return numBottles + x

# Let's create a variable x holding the number of bottles we've exchanged.
# This requires 'bottles' number of bottles to do:
# bottles = sum(numExchange + i for i in range(0, x))
#         = x*numExchange + x*(x-1)/2
#         = x*numExchange + x^2/2 - x/2

# Let's solve for x:
# x^2/2 - x*(2*numExchange - 1)/2 - bottles = 0

# We can also compute the number of bottles we can possibly create as:
# bottles = numBottles + x

# Giving our final equation:
# x^2/2 - x*(2*numExchange - 1)/2 - (numBottles + x) = 0
# x^2/2 - x*(2*numExchange - 3)/2 - numBottles       = 0
# x^2 - x*(2*numExchange - 3) - 2*numBottles         = 0

# Solve for x:
# a = 1, b = 2*numExchange - 3, c = -2*numBottles
#   (-(2*numExchange - 3) +- sqrt((2*numExchange - 3)^2 - 4*1*-2numBottles)) / 2*1
#-> (-2*numExchange + 3 +- sqrt(4*numExchange^2 - 12*numExchange + 9 + 8*numBottles)) / 2
#-> 3/2 - numExchange +- sqrt(4*numExchange^2 - 12*numExchange + 9 + 8*numBottles) / 4)
#-> 3/2 - numExchange +- sqrt(numExchange^2 - 3*numExchange + 2*numBottles + 9/4)

# We can see that most likely, the value of the right half is larger than the left,
# and as a negative number of bottles doesn't make sense, we can restrict the +-
# to only an addition (+). We cannot also have fractional bottles, as the decimal part
# does not count as a fully exchange bottle, and we will always end with a surplus of
# 1 bottle, if we can do any exchanges at all, thus we must apply a ceiling operation
# and decrement our number of exchanged bottles by 1, preserving its validity.
# This gives our final equation for the number of bottles exhanged x: 

# x = ceil(3/2 - numExchange + sqrt(numExchange^2 - numExchange + 9/4)) - 1

# Add this to our starting number of bottles numBottles, we result in the final
# number of bottles drank numBottles + x!