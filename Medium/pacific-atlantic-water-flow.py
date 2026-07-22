# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Using BFS
        m, n = len(heights), len(heights[0])

        # First, find all cells reachable from the Pacific
        queue = deque([(i, 0) for i in range(m)] + [(0, j) for j in range(n)])
        pacific = self.bfs(queue, heights, m, n)

        # Then, do the same but from the Atlantic
        queue = deque([(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)])
        atlantic = self.bfs(queue, heights, m, n)

        # Finally, return the cells reachable from both oceans
        return list(pacific.intersection(atlantic))
    
    def bfs(self, queue: deque[Tuple[int, int]], heights: List[List[int]], m: int, n: int) -> Set[Tuple[int, int]]:
        # Perform BFS, marking seen cells
        seen = set()
        while queue:
            i, j = queue.popleft()
            if (i, j) in seen:
                continue
            seen.add((i, j))
            
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not (0 <= i + a < m and 0 <= j + b < n):
                    continue
                
                # Only append the cell it can spill over us
                if heights[i][j] <= heights[i + a][j + b]:
                    queue.append((i + a, j + b))
        
        # Returning said seen cells
        return seen
