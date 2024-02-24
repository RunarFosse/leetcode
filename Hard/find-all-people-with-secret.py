# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(m+n)

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Using BFS

        # Create adjacency list
        adjls = [[] for _ in range(n)]
        for x, y, time in meetings:
            adjls[x].append((y, time))
            adjls[y].append((x, time))

        # Store earliest time any person knows the secret
        knows = [1e9] * n
        knows[0] = 0
        knows[firstPerson] = 0

        # Perform BFS starting from firstPerson and 0
        queue = deque([firstPerson, 0])
        while queue:
            person = queue.popleft()

            for meeting, time in adjls[person]:
                if time >= knows[person] and knows[meeting] > time:
                    knows[meeting] = time
                    queue.append(meeting)
        
        # Return everyone who know the secret
        return [i for i in range(n) if knows[i] < 1e9]