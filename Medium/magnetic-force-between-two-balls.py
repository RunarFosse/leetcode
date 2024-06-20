# Author: Runar Fosse
# Time complexity: O(n(log n + log a))
# Space complexity: O(n)

# where a is the maximum distance between any two baskets

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Using greedy
        n = len(position)

        # First sort basket positions in ascending order
        position.sort()

        # Then binary search to check if a solution exists for
        # a given minimum distance between ball baskets
        max_distance = 0
        left, right = 0, (position[-1] - position[0])+1
        while left < right:
            distance = (left + right) // 2

            # For this current distance, see if we can partition balls
            # into baskets of at least this distance apart 
            balls, last_position = m, -distance
            for i in range(n):
                if position[i] - last_position >= distance:
                    balls -= 1
                    last_position = position[i]
                    if not balls:
                        break
            
            # If we can place all balls, move left pointer
            if balls == 0:
                left = distance+1
                max_distance = max(distance, max_distance)
            # If not, move right
            else:
                right = distance
        
        return max_distance

# Simplified, this problem asks us to place m balls within n baskets such
# that the minimum distance between any two baskets containing a ball
# is maximized.