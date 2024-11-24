# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # Using greedy

        # Iterate the whole matrix
        total, negatives, smallest = 0, 0, 1e9
        for row in matrix:
            for element in row:
                # Keep track of the number of negative numbers
                if element < 0:
                    negatives += 1
                
                # Store the smallest element in absolute value
                smallest = min(abs(element), smallest)

                # And add to absolute sum
                total += abs(element)
    
        # Return the maximum matrix sum given optimal operations
        if negatives % 2:
            total -= 2 * smallest
        return total

# As we can multiply two neighbour numbers by -1, this means that, for every
# number of initial negative numbers in the matrix, we can always end up with
# either 1 or 0 negative numbers after performing optimal operations, and
# this depends on the parity of the number of negative numbers!

# Therefore the maximum matrix sum of the matrix is the absolute sum of
# the whole matrix, minus the twice the smallest absolute element, if and only
# if the number of initial negative numbers is odd!