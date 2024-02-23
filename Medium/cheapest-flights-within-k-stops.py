# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(m+n)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Using BFS

        # Create adjacency list
        adjls = [[] for _ in range(n)]
        for start, end, cost in flights:
            adjls[start].append((end, cost))
        
        # Use BFS to find shortest path
        min_price = [1e9] * n
        queue = deque([(src, 0, -1)])
        min_price[src] = 0
        while queue:
            node, total_price, visits = queue.popleft()

            # Stop exploring if having k stops
            if visits == k:
                continue

            # Add all neighbours and update their minimum price
            for neighbour, price in adjls[node]:
                if total_price + price < min_price[neighbour]:
                    min_price[neighbour] = total_price + price
                    queue.append((neighbour, total_price + price, visits + 1))
        
        # Return the cheapest flight if possible
        return -1 if min_price[dst] == 1e9 else min_price[dst]