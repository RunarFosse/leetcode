# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Using Union-Find
        n = len(stones)
        uf = self.UnionFind(n)
        
        # Add all stones to Union-Find datastructure
        rows, columns = {}, {}
        for i, (row, column) in enumerate(stones):
            # Connect them by shared rows or columns
            if row in rows:
                uf.union(i, rows[row])
            else:
                rows[row] = i
            
            if column in columns:
                uf.union(i, columns[column])
            else:
                columns[column] = i
        
        # Return the number of stones which can be removed
        return n - uf.disjoints

    class UnionFind:
        def __init__(self, n: int):
            self.parent = [i for i in range(n)]
            self.disjoints = n

        def find(self, i: int) -> int:
            if self.parent[i] != i:
                self.parent[i] = self.find(self.parent[i])

            return self.parent[i]
        
        def union(self, i: int, j: int) -> None:
            parent1 = self.find(i)
            parent2 = self.find(j)

            self.parent[parent1] = parent2

            # If two parents were unequal, they are now part of the same set
            if parent1 != parent2:
                self.disjoints -= 1


# If we use Union-Find, and connect stones which share a row or column.
# Then we can add all stones to the Union-Find datastructure and Cmpute how
# many disjoint sets we have. This will be the number of rocks remaining 
# after removing those which share rows/columns, meaning calculating
# how many stones we have removed is trivial.