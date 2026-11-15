# Author: Runar Fosse
# Time complexity: O(k + nlog k)
# Space complexity: O(k)

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Using greedy

        # Keep track of free servers in sorted order, as well as a heap of
        # servers currently processing a request
        servers, processing = SortedList(range(k)), []

        # Also keep track of the servers with maximal request handle count
        maximum, busiest = 0, []

        # Then iterate every request
        handled = [0] * k
        for i, (time, duration) in enumerate(zip(arrival, load)):
            # Reclaim any servers which have finished processing a request
            while processing and processing[0][0] <= time:
                _, server = heappop(processing)
                servers.add(server)
            
            # If there are no free servers, drop the current request
            if not servers:
                continue

            # Otherwise, find the next available server to handle this request
            index = servers.bisect_left(i % k)
            server = servers.pop(index) if index < len(servers) else servers.pop(0)

            # Increment its request handle count, and set away for processing
            handled[server] += 1
            heappush(processing, (time + duration, server))
        
            # And remember the servers with the maximal request handle count
            if handled[server] > maximum:
                maximum = handled[server]
                busiest = [server]
            elif handled[server] == maximum:
                busiest.append(server)

        # Finally, return these busiest servers
        return busiest
