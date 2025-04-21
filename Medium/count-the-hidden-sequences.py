# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)

        # Compute the hidden sequence with 0 as our initial element
        hidden = [0] * (n + 1)
        smallest = largest = 0
        for i in range(n):
            element = differences[i] + hidden[i]
            hidden[i + 1] = element

            # Store smallest and largest hidden element
            smallest = min(element, smallest)
            largest = max(element, largest)
        
        # Move the hidden sequence such that the
        # smallest element is equal to the lower bound
        difference = lower - smallest
        smallest += difference
        largest += difference

        # Finally, return the number of possible hidden sequences we can create
        return max(upper - largest + 1, 0)
