# Author: Runar Fosse
# Time complexity: O(n+m)
# Space complexity: O(1)

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Using Floyd-Warshall
        indexOf = lambda c : ord(c) - ord("a")

        # First initialize the distance matrix correctly
        distances = [[1e9] * 26 for _ in range(26)]
        for i in range(26):
            distances[i][i] = 0

        # And populate it with the given conversion costs
        for src, dest, distance in zip(original, changed, cost):
            current_distance = distances[indexOf(src)][indexOf(dest)]
            distances[indexOf(src)][indexOf(dest)] = min(distance, current_distance)
        
        # Then for each letter, calculate the cost of converting to
        # every other letter, using any letter as an "intermediate" node
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    new_distance = distances[i][k] + distances[k][j]
                    distances[i][j] = min(new_distance, distances[i][j])
        
        # Then iterate the input string, computing
        # total cost of converting it to target
        total_cost = 0
        for src, tar in zip(source, target):
            cost = distances[indexOf(src)][indexOf(tar)]

            # If cost is infinite, conversion is not possible
            if cost == 1e9:
                return -1
            total_cost += cost

        # Return final conversion cost
        return total_cost