# Author: Runar Fosse
# Time complexity: O(mlog n + n)
# Space complexity: O(m + n)

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # First, initialize the graph with a loop back to every node
        adjls = [[i] for i in range(n)]

        # Then, add edges to the graph
        for a, b in edges:
            adjls[a].append(b)
            adjls[b].append(a)
        
        # Now, iterate every node's outgoing edges
        frequencies = defaultdict(int)
        for i in range(n):
            # Count the outgoing edges as a component "fingerprint"
            outgoing = tuple(sorted(adjls[i]))

            # And store the frequency of each such fingerprint
            frequencies[outgoing] += 1
        
        # Finally, iterate each such component fingerprint
        completes = 0
        for component, frequency in frequencies.items():
            # If the size of a component is equal to the frequency of its fingerprint
            if len(component) == frequency:
                # Then we identified a complete connected component
                completes += 1
        
        # Finally, return the count of these complete connected components
        return completes
