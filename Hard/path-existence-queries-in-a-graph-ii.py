# Author: Runar Fosse
# Time complexity: O((m + n)log n)
# Space complexity: O(m + nlog n)

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Using binary lifting

        # First, sort the nodes in ascending order of node weight
        nodes = sorted(enumerate(nums), key=lambda e: e[1])
        indices = [0] * n
        for i, (node, _) in enumerate(nodes):
            indices[node] = i
        
        # Then, find the direct parent of each of the nodes for binary lifting
        max_power = n.bit_length()
        up, right = [[0] * max_power for _ in range(n)], 0
        for i in range(n):
            if right < i:
                right = i
            
            # By moving the right pointer to the last directly connected node
            while right < n - 1 and nodes[right + 1][1] - nodes[i][1] <= maxDiff:
                right += 1
            up[i][0] = right
        
        # Then, populate the rest of the binary lifting table
        for power in range(1, max_power):
            # By iterating each node and updating parents in increasing power
            for i in range(n):
                middle = up[i][power - 1]
                up[i][power] = up[middle][power - 1]

        # Finally, iterate each of the queries
        answer = []
        for u, v in queries:
            # First, get the new indices of each of the nodes
            i, j = indices[u], indices[v]
            if i == j:
                answer.append(0)
                continue
            
            # Force i to be the smaller node
            if j < i:
                i, j = j, i
            
            # And lift i until i and j are directly adjacent (if possible)
            node, distance = i, 0
            for power in reversed(range(max_power)):
                if up[node][power] < j:
                    node = up[node][power]
                    distance += (1 << power)
            
            # If j is not within the direct neighbourhood of node
            if up[node][0] < j:
                # They are not in the same connected component
                answer.append(-1)
            else:
                # Otherwise, we can traverse directly from node to j in 1 step
                answer.append(distance + 1)

        # At last, return the answer to each of the queries
        return answer


# Instead of storing the node connections as a graph, we can instead store the furthest
# most node connection (rightwards in the array) as a node's "parent", thus representing
# node connections as a tree structure rather than an explicit graph.
# Then, we can interpret that node is directly connected to all nodes between itself
# and its direct parent in the tree. This then also allow efficient for component 
# checking and distances within said component using binary lifting.