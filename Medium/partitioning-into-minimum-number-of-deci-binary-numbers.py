# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minPartitions(self, n: str) -> int:
        # Iterate the string
        largest = 0
        for c in n:
            # Storing the largest digit in the string
            largest = max(int(c), largest)

            # If we ever reach 9, the largest possible digit value
            if largest == 9:
                # Break out early
                break
        
        # Finally, return this largest digit
        return largest


# It is obvious that the number of positive deci-binary numbers needed to sum
# up to n is equal to the value of the largest digit in n.
# This is because the largest digit x has to be covered by the 
# sum of x deci-binary numbers. All other digits can be covered in these x numbers.

# Example:
# = 32401
# + 11101
# + 11100
# + 10100
# + 00100

# Thus, 32401 is covered by 4 deci-binary numbers, equal to its largest digit, 4.