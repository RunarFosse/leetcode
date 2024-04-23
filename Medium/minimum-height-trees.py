# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Using BFS/DFS

        # Create an adjacency list
        adjls = [[] for _ in range(n)]
        for a, b in edges:
            adjls[a].append(b)
            adjls[b].append(a)
        
        # Then use BFS from node 0 to find any node furthest out in the tree
        queue = deque([0])
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)

            for neighbour in adjls[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
        
        # The last node ever visited in the search is far away
        # Perform DFS from this node and store the longest path
        current_path, longest_path = [], []
        queue = [(0, node)]
        visited.clear()
        while queue:
            depth, node = queue.pop()
            visited.add(node)

            # Keep track of current path
            while depth < len(current_path):
                current_path.pop()
            current_path.append(node)
            # And remember it if it is longest
            if len(current_path) > len(longest_path):
                longest_path = current_path[:]

            for neighbour in adjls[node]:
                if neighbour not in visited:
                    queue.append((depth+1, neighbour))

        # Return the middle node(s) of the longest path
        longest_length = len(longest_path)
        minimal_roots = [longest_path[longest_length // 2]]
        if not longest_length % 2:
            minimal_roots.append(longest_path[longest_length // 2 - 1])
        return minimal_roots
        
# This is a maximal path problem, where the root node(s) of a minimum height
# tree are the node(s) in the middle of the maximal path in said graph.