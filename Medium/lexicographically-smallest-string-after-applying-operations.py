# Author: Runar Fosse
# Time complexity: O(n^3)
# Space complexity: O(n^2)

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # Using BFS
        n = len(s)

        # Turn the string into a tuple of integers, and add it to a deque
        string = tuple(int(c) for c in s)
        queue = deque([string])

        # Perform BFS
        smallest, seen = string, set()
        while queue:
            string = queue.popleft()
            if string in seen:
                continue
            seen.add(string)

            # Store the lexicographically smallest string
            if string < smallest:
                smallest = string

            # Perform both operations, and add them back into the queue
            new = list(string)
            for i in range(n):
                if i % 2:
                    new[i] = (string[i] + a) % 10
            queue.append(tuple(new))

            new = list(string)
            for i in range(n):
                new[i] = string[(i - b) % n]
            queue.append(tuple(new))

        # Finally, return the lexicographically smallest string
        return "".join(str(c) for c in smallest)