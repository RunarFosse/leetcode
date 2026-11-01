# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Using Union-Find
        n = len(nums)

        # Compute the digit sum of each element
        digitsums = [0] * n
        for i in range(n):
            num, digitsum = nums[i], 0
            while num:
                digitsum += num % 10
                num //= 10
            digitsums[i] = digitsum
        
        # Sort the digit sums in correct order
        indices = sorted([i for i in range(n)], key=lambda i: (digitsums[i], nums[i]))

        # For each element, find their correct resulting index
        correct = [0] * n
        for i in range(n):
            correct[indices[i]] = i
        
        # Then, use Union-Find and find cycles in position swaps
        uf = UnionFind(n)
        for i in range(n):
            uf.union(i, correct[i])
        
        # The minimum number of swaps is equal to the complement of 
        # the number of disjoint components
        return n - uf.components


class UnionFind():
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [0] * n
        self.components = n
    
    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i1: int, i2: int) -> None:
        parent1, parent2 = self.find(i1), self.find(i2)
        if parent1 == parent2:
            return
        
        if self.size[parent1] < self.size[parent2]:
            parent1, parent2 = parent2, parent1
        
        self.parent[parent2] = parent1
        self.size[parent1] += self.size[parent2]
        self.components -= 1
