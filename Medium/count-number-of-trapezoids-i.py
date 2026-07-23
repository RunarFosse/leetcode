# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # First, count the number of points at each y-coordinate
        horizontals = defaultdict(int)
        for _, y in points:
            horizontals[y] += 1
        
        # Then, for each y-coordinate, compute and sum over number of trapezoids
        trapezoids, previous = 0, 0
        for points in horizontals.values():
            # Compute the number of ways to choose two current points
            pairs = points * (points - 1) // 2

            # Multiply this together with previously seen pairs to find trapezoids
            trapezoids = (trapezoids + pairs * previous) % self.mod

            # And add these pairs to previously seen
            previous = (previous + pairs) % self.mod
        
        # Finally, return the total number of possible horizontal trapezoids
        return trapezoids


# The formula for n choose 2 is equal to :
# n! / 2!(n - 2)! = (n * (n - 1) * (n - 2)!) / (2 * 1 * (n - 2)!)
#                 = (n * (n - 1)) / 2

# This can be used to find the number of ways to choose two values,
# i.e. a pair, from n different values.