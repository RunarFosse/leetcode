# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Using BFS

        # First create a graph
        adjls = defaultdict(list)
        for a, b in edges:
            adjls[a].append(b)
            adjls[b].append(a)
        
        # Use BFS to find the minimum (and consequently second)
        # time to go from vertex 1 to n
        queue = deque([(1, 0)])
        first_visit, second_visit = defaultdict(int), defaultdict(int)
        while queue:
            node, total_time = queue.popleft()

            # Check if we need to wait until light is green
            is_red = (total_time // change) % 2
            if is_red:
                total_time += change - total_time % change     
            
            # Add all neighbours to queue
            total_time += time
            for neighbour in adjls[node]:
                # Note first distinct time visit to the neighbour
                if not first_visit[neighbour]:
                    first_visit[neighbour] = total_time
                    queue.append((neighbour, total_time))
                
                # As well as second, returning if this is the end node
                elif not second_visit[neighbour] and first_visit[neighbour] != total_time:
                    if neighbour == n:
                        return total_time

                    second_visit[neighbour] = total_time
                    queue.append((neighbour, total_time))
