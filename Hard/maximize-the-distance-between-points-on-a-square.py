# Author: Runar Fosse
# Time complexity: O(nk(log n)(log m))
# Space complexity: O(n)

# where m is the side length

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Using binary search
        n, perimeter = len(points), 4 * side

        # Iterate all the points
        distances = []
        for x, y in points:
            # Storing them as anticlockwise Manhattan distance from the origin
            distance = x + y
            if y > x:
                distance = perimeter - distance
            distances.append(distance)
        
        # Sort the distances in ascending order
        distances.sort()

        # Binary search the maximum minimum Manhattan distance between k points
        left, right = 0, perimeter
        while left < right:
            pivot = (left + right) // 2

            # Check if we can choose k points with at most this distance
            valid = False
            for start in distances:
                current, end = start, start + perimeter - pivot
                for _ in range(k - 1):
                    # Binary search the closest point after this distance
                    index = bisect_left(distances, current + pivot)
                    if index >= n or distances[index] > end:
                        current = -1
                        break
                    current = distances[index]
                
                # If the current point is non-sentinel, we've found a valid k-selection
                if current >= 0:
                    valid = True
                    break

            # And move bounds based on the result
            if valid:
                left = pivot + 1
            else:
                right = pivot
        
        # And return the maximum possible minimum Manhattan distance between k points
        return left - 1
