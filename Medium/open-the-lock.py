# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Using BFS
        visited = set(deadends)

        # Easy edge case check (if target is in deadends it can't be reached)
        if target in visited:
            return -1

        # Perform BFS
        queue = deque([(0, "0000")])
        while queue:
            turns, state = queue.popleft()
            if state == target:
                return turns
            
            # Skip if state has been visited before
            if state in visited:
                continue
            visited.add(state)

            # Add all neighbour states to queue
            chars = list(state)
            for i in range(4):
                digit = ord(chars[i]) - ord("0")

                # Rotate current wheel up
                chars[i] = chr((digit + 1) % 10 + ord("0"))
                queue.append((turns+1, "".join(chars)))

                # Rotate current wheel down
                chars[i] = chr((digit - 1) % 10 + ord("0"))
                queue.append((turns+1, "".join(chars)))

                # Reset before going to next wheel
                chars[i] = chr(digit + ord("0"))

        # If state cannot be found, return -1
        return -1
