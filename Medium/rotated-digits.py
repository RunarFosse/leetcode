# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Using dynamic programming
        opt = [0] * (n + 1)

        # Declare the base case encodings
        good = 0
        for i in range(min(10, n + 1)):
            if i in [3, 4, 7]:
                opt[i] = -1
            elif i in [0, 1, 8]:
                opt[i] = 1
            else:
                opt[i] = 2
                good += 1

        # Iterate the rest of the numbers
        for i in range(10, n + 1):
            # Split the number in two
            left = opt[i // 10]
            right = opt[i % 10]

            # If either side is invalid, the current is too
            if left == -1 or right == -1:
                opt[i] = -1
            
            # If both sides are valid, but not good, the current is too
            elif left == 1 and right == 1:
                opt[i] = 1
            
            # Finally, if either side is then good, the current is too
            else:
                opt[i] = 2
                good += 1
        
        # Finally, return the number of good integers
        return good


# opt(i) - Encodes if i is a good, valid or invalidly rotated integer.
#          Encodings are 1 if good, 0 if valid, -1 if invalid.

# Base case:
# opt({3, 4, 7}) = -1 
# opt({0, 1, 8}) = 1
# opt({2, 5, 6, 9}) = 2

# Recurrency:
# opt(i) | left == -1 or right == -1 = -1
#        | left == 1 and right == 1 = 1
#        | otherwise = 2
#         where left = opt(i // 10)
#               right = opt(i % 10)

# Then just sum all numbers which have an encoding of 2!

# N.o. states = n
# Time complexity per state -> O(1)
# Total time complexity => O(n)