# Author: Runar Fosse
# Time complexity: O(klog k + mnlog(mn))
# Space complexity: O(k + mn)

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # Using BFS
        m, n, k = len(grid), len(grid[0]), len(queries)

        # Sort queries in increasing order
        queries = sorted([(queries[index], index) for index in range(k)])
        
        # Store the answers in their initial order
        answers = [0] * k

        # Then, for each query
        queue, skipped, seen = deque([]), [(grid[0][0], 0, 0)], set()
        for query, index in queries:
            # First, add all reachable cells from skipped to queue
            while skipped and skipped[0][0] < query:
                _, i, j = heappop(skipped)
                queue.append((i, j))

            # Continue BFS
            while queue:
                i, j = queue.popleft()

                # If we cannot visit this cell during this query, add to skipped
                if grid[i][j] >= query:
                    heappush(skipped, (grid[i][j], i, j))
                    continue

                # If not, visit by adding to seen
                if (i, j) in seen:
                    continue
                seen.add((i, j))

                # And add neighbours
                for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if i + a < 0 or i + a >= m or j + b < 0 or j + b >= n:
                        continue
                    queue.append((i + a, j + b))

            # Count current answer as no. visited nodes
            answers[index] = len(seen)
            last = query
        
        # Finally, return the answers
        return answers