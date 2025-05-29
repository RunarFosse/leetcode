# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # Using BFS
        n, m = len(edges1), len(edges2)

        # First, create both graphs
        adjls1 = defaultdict(list)
        for a, b in edges1:
            adjls1[a].append(b)
            adjls1[b].append(a)
        adjls2 = defaultdict(list)
        for u, v in edges2:
            adjls2[u].append(v)
            adjls2[v].append(u)

        # Then, colour each node in each graph either odd or even,
        # and count each graphs total
        colours1, odds1, evens1 = self.colour(adjls1)
        colours2, odds2, evens2 = self.colour(adjls2)

        # For the second graph, only count most populated colour as target
        targets2 = max(odds2, evens2)

        # Finally, for each node in graph1, count equal colour in graph1,
        # opposite colour in graph2, that is its number of targets, and return
        targets1 = []
        for i in range(n + 1):
            colour = colours1[i]
            targets1.append((odds1 if colour % 2 else evens1) + targets2)
        return targets1

    def colour(self, adjls: List[int]) -> Tuple[Dict[int, int], int, int]:
        # Colour a graph
        queue = deque([(0, 0)])
        colours, odds, evens = {}, 0, 0
        while queue:
            node, colour = queue.popleft()
            if node in colours:
                continue

            # Colour a node either odd or even, and keep total count
            colours[node] = colour % 2
            if colour % 2:
                odds += 1
            else:
                evens += 1

            for neighbour in adjls[node]:
                queue.append((neighbour, colour + 1))

        return colours, odds, evens
        