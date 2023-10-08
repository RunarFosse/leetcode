# Author: Runar Fosse
# Time complexity: O(n!)
# Space complexity: O(n!)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        return self.permuteHelper(set())
    
    def permuteHelper(self, seen: Set[int]) -> List[List[int]]:
        permutations = []
        current_seen = set()
        for i, n in enumerate(self.nums):
            if seen.issuperset({i}) or current_seen.issuperset({n}):
                continue
            
            new_seen = seen.copy()
            new_seen.add(i)
            permutations += [[n] + perm for perm in self.permuteHelper(new_seen)]
            current_seen.add(n)

        if not permutations:
            return [[]]    
        
        return permutations