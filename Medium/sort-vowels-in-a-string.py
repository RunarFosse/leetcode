# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def sortVowels(self, s: str) -> str:
        # Using Counting sort
        vowel_string = "AEIOUaeiou"

        # First count occurence of each vowel
        vowels = set(vowel_string)
        counts = defaultdict(lambda : 0)
        for c in s:
            if c in vowels:
                counts[c] += 1
        
        # Then recreate string, substituting vowels for sorted order
        vowels_sorted = deque(vowel_string)
        string = ""
        for c in s:
            if c in vowels:
                while not counts[vowels_sorted[0]]:
                    vowels_sorted.popleft()
                string += vowels_sorted[0]
                counts[vowels_sorted[0]] -= 1
            else:
                string += c

        return string