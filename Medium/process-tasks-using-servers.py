# Author: Runar Fosse
# Time complexity: O(mlog n + n)
# Space complexity: O(m + n)

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Using greedy
        n, m = len(servers), len(tasks)

        # Make the server a heap, sorted in ascending order of weight
        servers = [(servers[i], i) for i in range(n)]
        heapify(servers)

        time, offset = 0, 0
        processing, answers = [], [None] * m
        while time < m:
            # First, reclaim any servers that have finished processing
            while processing and processing[0][0] <= time + offset:
                _, server = heappop(processing)
                heappush(servers, server)

            # If there aren't any free servers
            if not servers:
                # Wait until the next server has finished processing
                offset = processing[0][0] - time
                continue

            # Otherwise, assign this task to the smallest weight free server
            server = heappop(servers)
            answers[time] = server[1]

            # Adding it to the processing heap
            heappush(processing, (time + tasks[time] + offset, server))

            # Then update the time, and decrement a current potential offset
            time += 1
            offset = max(0, offset - 1)

        # Finally, return the server index for which each task is assigned to
        return answers
