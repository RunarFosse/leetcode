# Author: Runar Fosse
# Time complexity: O(n + k^2)
# Space complexity: O(n + k)

class Solution:
    mod = int(1e9 + 7)
    def possibleStringCount(self, word: str, k: int) -> int:
        # Using dynamic programming
        n = len(word)

        # First, count number of adjacent characters
        characters = [1]
        for i in range(1, n):
            if word[i] == word[i - 1]:
                characters[-1] += 1
            else:
                characters.append(1)
        
        # Then, compute the total number of possible strings
        strings = reduce(lambda r, e: e * r % self.mod, characters, 1)

        # If the smallest string is larger than k, return all possible strings
        if len(characters) >= k:
            return strings
        
        # Otherwise, iterate over every duplicate character interval
        prefixes = [1] * k
        for i in range(len(characters)):
            # Compute how many ways we can get a string with exactly j characters
            lengths = [0] * k
            for j in range(1, k):
                lengths[j] = prefixes[j - 1]
                if j - characters[i] >= 1:
                    lengths[j] -= prefixes[j - characters[i] - 1]
                    lengths[j] %= self.mod

            # And compute prefixes array of all strings of less or equal length
            prefixes_new = [lengths[0]] + [0] * (k - 1)
            for j in range(1, k):
                prefixes_new[j] = (prefixes_new[j - 1] + lengths[j]) % self.mod
            prefixes = prefixes_new
        
        # Finally, subtract the number of strings with a length less than k and return
        return (strings - prefixes[k - 1]) % self.mod
        