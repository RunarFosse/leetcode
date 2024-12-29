# Author: Runar Fosse
# Time complexity: O(mn + mj)
# Space complexity: O(mn)

# where j is the total number of words

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # Using dynamic programming
        self.n, self.m = len(target), len(words[0])

        # First compute the frequency of each letter of the dictionary,
        # at every index
        self.frequencies = [[0] * 26 for _ in range(self.m)]
        indexOf = lambda c: ord(c) - ord("a")
        for j in range(self.m):
            for word in words:
                self.frequencies[j][indexOf(word[j])] += 1
        
        # Then compute the number of ways using dynamic programming
        self.target = [indexOf(c) for c in target]
        return self.opt(0, 0)
    
    @functools.cache
    def opt(self, i: int, k: int) -> int:
        # If we've reached the end, return
        if i == self.n:
            return 1
        if k == self.m:
            return 0

        # Get the current letter we have to form
        current = self.target[i]

        # Compute ways by forming using the k'th index
        ways = self.frequencies[k][current] * self.opt(i + 1, k + 1)

        # Or by using a later k
        ways += self.opt(i, k + 1)

        # Finally, return modulo 1e9 + 7
        return ways % int(1e9 + 7)