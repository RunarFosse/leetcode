# Author: Runar Fosse
# Time complexity: O(n^3)
# Space complexity: O(n^2)

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Using Floyd-Warshall

        # Initialize and populate the distance matrix
        distances = [[1e9] * n for _ in range(n)]
        for a, b, distance in edges:
            distances[a][b] = distance
            distances[b][a] = distance
        
        # Calculate the distance from every city to every city
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    new_distance = distances[i][k] + distances[k][j]
                    distances[i][j] = min(new_distance, distances[i][j])
        
        # Then for every city, count and find the city with the least
        # number of cities within the given range
        loneliest_city, min_close_neighbours = None, n
        for i in range(n):
            close_neighbours = sum(1 for distance in distances[i]
                                    if distance <= distanceThreshold)

            if close_neighbours <= min_close_neighbours:
                if close_neighbours == min_close_neighbours:
                    loneliest_city = max(i, loneliest_city)
                else:
                    loneliest_city = i
                min_close_neighbours = close_neighbours
        
        # Return the city with the least neighbour cities within range
        return loneliest_city