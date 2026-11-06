# Author: Runar Fosse
# Time complexity: O(mlog m + klog k)
# Space complexity: O(m + n + k)

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Using sliding window
        m, k = len(logs), len(queries)

        # Sort the logs and queries in ascending order of time
        logs.sort(key=lambda e: e[1])
        queries = sorted(enumerate(queries), key=lambda e: e[1])

        # Then, keep a sliding window of server's with recent requests
        start, index, results = 0, 0, [None] * k
        servers, requests = set(), defaultdict(int)
        for server, time in logs:
            # If we're at the time of the next query
            while index < k and time > queries[index][1]:
                # Shrinking the window if it is bigger than x
                while queries[index][1] - x > logs[start][1]:
                    old_server = logs[start][0]
                    requests[old_server] -= 1
                    if not requests[old_server]:
                        servers.remove(old_server)
                    start += 1
                
                # And storing the query result
                results[queries[index][0]] = n - len(servers)
                index += 1
            
            # Expand the window with this new server
            servers.add(server)
            requests[server] += 1
        
        # Iterate the rest of the queries
        while index < k:
            # Shrinking the window if it is bigger than x
            while start < m and queries[index][1] - x > logs[start][1]:
                old_server = logs[start][0]
                requests[old_server] -= 1
                if not requests[old_server]:
                    servers.remove(old_server)
                start += 1
                
            # And storing the query result
            results[queries[index][0]] = n - len(servers)
            index += 1

        # Finally, return the answer to all the queries
        return results
