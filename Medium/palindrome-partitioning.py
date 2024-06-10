# Author: Runar Fosse
# Time complexity: O(n^32^n)
# Space complexity: O(2^n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Using dynamic programming
        self.n, self.s = len(s), s
        return self.opt(0)

    @functools.cache
    def opt(self, i: int) -> List[List[str]]:
        if i == self.n:
            return [[]]
        
        # Compute all palindrome partitions starting from index i
        partitions = []
        for j in range(i, self.n):
            substring = self.s[i:j+1]
            if self.isPalindrome(substring):
                for partition in self.opt(j+1):
                    partitions.append([substring] + partition)

        # And return them
        return partitions
        
    def isPalindrome(self, s: str) -> bool:
        # Check that a given string is palindromic
        p1, p2 = 0, len(s)-1
        while p1 <= p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True


# opt(i) - All palindrome partitionings for s[i:]

# Base case:
# opt(n) = [[]]

# Recurrency:
# opt(i) = ([s[i:j+1]] + partition for j in range(i, n) 
#           if s[i:j+1] is palindromic for partition in opt(j+1))