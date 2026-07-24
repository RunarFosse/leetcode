# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # Using sliding window
        n = len(word)

        # Store the frequency of all vowels in the window
        vowels = {c: 0 for c in "aeiou"}

        # Then, slide a window over the word
        substrings, start = 0, 0
        consonants, distincts, extras = 0, 0, 0
        for end in range(n):
            # Expand the window
            if word[end] in vowels:
                vowels[word[end]] += 1
                if vowels[word[end]] == 1:
                    distincts += 1
            else:
                consonants += 1
            
            # While we have too many consonants, shrink the window
            while consonants > k:
                if word[start] in vowels:
                    vowels[word[start]] -= 1
                    if vowels[word[start]] == 0:
                        distincts -= 1
                else:
                    consonants -= 1
                start += 1
                extras = 0
            
            # Count every valid substring within
            while distincts == 5 and consonants == k:
                # Stop if we hit a consonant
                if word[start] not in vowels or vowels[word[start]] <= 1:
                    break

                # Otherwise, count extra vowels allowing for many valid substrings within
                extras += 1
                vowels[word[start]] -= 1
                start += 1

            # And if the current window has at least a valid substring
            if distincts == 5 and consonants == k:
                # Count it, plus any extras
                substrings += 1 + extras
        
        # Finally, return the number of such valid substrings
        return substrings
