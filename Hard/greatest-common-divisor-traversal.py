# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(n)

# m represents the maximum entry in nums array
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # Early return if list only contains 1 number
        if len(nums) == 1:
            return True

        # Extract every unique number
        max_entry = 0
        numbers = set()
        for num in nums:
            # Early return as 1 is coprime with every other number
            if num == 1:
                return False
            numbers.add(num)
            max_entry = max(num+1, max_entry)

        # Create a sieve, storing greates prime factor of each number
        sieve = [0] * max_entry
        for i in range(2, max_entry):
            if not sieve[i]:
                for factor in range(i, max_entry, i):
                    sieve[factor] = i

        # Create a Graph with extra dummy nodes
        union = UnionFind(2*max_entry-1)
        for num in nums:
            current = num
            while current > 1:
                greatest_factor = sieve[current]
                dummy_root = max_entry-1 + greatest_factor
                if union.find(num) != union.find(dummy_root):
                    union.merge(num, dummy_root)
                while not current % greatest_factor:
                    current //= greatest_factor
        
        # Then extract all distinct connected components
        components = 0
        for num in range(2, max_entry):
            if num in numbers and union.find(num) == num:
                components += 1
        
        # Graph is fully connected if containing only 1 component
        return components == 1

# Union-Find implementation
# with union by rank and path compression
class UnionFind:
    def __init__(self, size):
        self.root = []
        self.size = []
        for i in range(size+1):
            self.root.append(i)
            self.size.append(1)
    
    def find(self, node):
        if self.root[node] == node:
            return node
        
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def merge(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return
        
        if self.size[parent2] > self.size[parent1]:
            parent1, parent2 = parent2, parent1
        
        self.root[parent2] = parent1
        self.size[parent1] += self.size[parent2]