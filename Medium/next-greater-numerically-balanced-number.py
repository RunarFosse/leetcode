# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(log n)

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # Using brute force

        # Find the first beautiful number larger than n
        while not self.isBeautiful(n + 1):
            n += 1
        return n + 1
    
    def isBeautiful(self, i: int) -> bool:
        # Check if a number is beautiful, by counting the frequency of its digits
        frequencies = defaultdict(int)
        while i:
            frequencies[i % 10] += 1
            i //= 10

        # And checking that the frequency of each occuring digit matches itself
        return all(frequency == digit for digit, frequency in frequencies.items())