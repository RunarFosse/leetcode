# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Count how many people are trusted by and how many they trust
        trusted = [0] * n
        trusts = [0] * n
        for a, b in trust:
            trusted[a-1] += 1
            trusts[b-1] += 1
        
        # For every person
        for person in range(n):
            # If a person trusts no one and is trusted by everyone else
            if not trusted[person] and trusts[person] == n-1:
                # Then they are a town judge
                return person+1
        
        return -1
