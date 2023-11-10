# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Using DAG

        # Create graph
        adjs = {}
        for u, v in adjacentPairs:
            if not adjs.get(u):
                adjs[u] = []
            if not adjs.get(v):
                adjs[v] = []
            
            adjs[u].append(v)
            adjs[v].append(u)
        
        # Find root
        for node, neighbours in adjs.items():
            if len(neighbours) == 1:
                root = node
                break
        
        # Restore array
        array = []
        last, current = root, root
        while True:
            array.append(current)

            if len(adjs.get(current)) == 1 and current != root:
                break

            for neighbour in adjs.get(current):
                if neighbour != last:
                    last = current
                    current = neighbour
                    break
        
        return array
            
        

# First create a DAG, then find a root (which will be the start/end of list).
# Then just traverse using a graph search and construct the list!