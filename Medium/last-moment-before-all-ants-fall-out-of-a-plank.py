# Author: Runar Fosse
# Time complexity: O(n+m)
# Space complexity: O(1)

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        maxdistance = 0
        for index in left:
            maxdistance = max(index, maxdistance)
        for index in right:
            maxdistance = max(n-index, maxdistance)
        
        return maxdistance


# An important observation is that if two or more ants collide, they change direction.
# This is in practice equal to if they all just continued walking over eachother.
# Therefore we can disregard change of direction completely and only solve the
# basic problem.

# This solution is finding the ant furthest from any edge. Its distance is the answer.