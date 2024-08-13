# Author: Runar Fosse
# Time complexity: O(2^n)
# Space complexity: O(2^n)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Using DFS
        self.combinations = []

        # Sort to avoid duplicates and greedily escape finished searches
        self.candidates, self.n = sorted(candidates), len(candidates)

        self.dfs(0, target, [])
        return self.combinations
    
    def dfs(self, i: int, target: int, stack: List[int]) -> None:
        if target <= 0 or i == self.n:
            if target == 0:
                self.combinations.append(stack)
            return
        
        # Iterate and search all elements which come after current
        for j in range(i, self.n):
            candidate = self.candidates[j]
            if j > i and candidate == self.candidates[j-1]:
                continue
            self.dfs(j+1, target - candidate, stack + [candidate])
        