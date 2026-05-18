# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        # Using BFS
        n = len(nums)

        # Iterate the array, finding the maximum entry, and indices of all elements
        indices = defaultdict(list)
        for i in range(n):
            indices[nums[i]].append(i)

        # Finally, perform BFS
        queue, seen = deque([(0, 0)]), set()
        while queue:
            i, distance = queue.popleft()
            if i in seen:
                continue
            seen.add(i)
            
            # If we are at the end, return the minimum distance
            if i == n - 1:
                return distance
            
            # Add valid adjacent steps to queue
            if i > 0:
                queue.append((i - 1, distance + 1))
            queue.append((i + 1, distance + 1))

            # As well as all equal valued positions
            for neighbour in indices[nums[i]]:
                queue.append((neighbour, distance + 1))

            # Optimize by removing visited neighbours
            indices[nums[i]].clear()
