# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Using two pass
        n = len(ratings)

        # Store the number of candy each child gets, and initialize with 1
        candy = [1] * n

        # Then, perform a left-to-right pass
        for i in range(1, n):
            # If a child has a higher rating than the previous
            if ratings[i] > ratings[i - 1]:
                # Give out one more candy
                candy[i] = candy[i - 1] + 1
        
        # Then, a right-to-left pass
        for i in reversed(range(n - 1)):
            # Doing the same, but in other direction
            if ratings[i] > ratings[i + 1]:
                # Give out one more candy, but only if it is larger than last
                candy[i] = max(candy[i + 1] + 1, candy[i])
        
        # Finally, return the sum of all the candy
        return sum(candy)
        