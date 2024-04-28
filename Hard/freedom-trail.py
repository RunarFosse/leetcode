# Author: Runar Fosse
# Time complexity: O(mnlog(mn))
# Space complexity: O(mn)

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Using Djikstra's
        n, m = len(ring), len(key)

        # First store all indices of each character in ring
        indices = defaultdict(list)
        for i, c in enumerate(ring):
            indices[c].append(i)

        # Search shortest path from key[0] to key[m]
        queue = [(0, 0, 0)]
        heapify(queue)
        visited = set()
        while queue:
            steps, ring_index, key_index = heappop(queue)

            # If seen same state, continue
            if (ring_index, key_index) in visited:
                continue
            visited.add((ring_index, key_index))

            # If we reach end of key, we have found minimum steps to solve
            if key_index == m:
                return steps

            # Add all possible rotations to iterate key word to queue
            for i in indices[key[key_index]]:
                rotations = min(abs(ring_index - i), n - abs(ring_index - i))
                heappush(queue, (steps + rotations + 1, i, key_index+1))
        