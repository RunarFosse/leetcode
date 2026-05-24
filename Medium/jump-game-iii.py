# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # Using BFS
        n = len(arr)

        # We initially start at the start index
        queue, seen = deque([start]), set()

        # Then, start BFS
        while queue:
            i = queue.popleft()
            if i in seen:
                continue
            seen.add(i)

            # If we are at a value of 0, return True
            if arr[i] == 0:
                return True

            # Add all neighbours to the queue
            if i - arr[i] >= 0:
                queue.append(i - arr[i])
            if i + arr[i] < n:
                queue.append(i + arr[i])
        
        # If loop terminates, we cannot reach an element valued 0
        return False
