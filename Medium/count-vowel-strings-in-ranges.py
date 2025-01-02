# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Using prefix sum
        vowels = "aeiou"

        # First, count prefix sum of words that start and end with vowels
        prefixes = [0]
        for word in words:
            prefixes.append(prefixes[-1])

            start, end = word[0], word[-1]
            if start in vowels and end in vowels:
                prefixes[-1] += 1
        
        # Then for every query, compute vowel strings in range
        answers = []
        for start, end in queries:
            answers.append(prefixes[end + 1] - prefixes[start])

        return answers