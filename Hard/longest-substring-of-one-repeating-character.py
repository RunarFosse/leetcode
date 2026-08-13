# Author: Runar Fosse
# Time complexity: O((m + n)log n)
# Space complexity: O(n)

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # Using sorted list
        n = len(s)

        # First, iterate the initial string
        substrings, lengths, i = SortedList(), SortedList(), 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            
            # Storing substrings of repeated characters and their lengths
            substrings.add((i, j - 1))
            lengths.add(j - i)
            i = j
        
        # Then, iterate the queries
        answers, characters = [], list(s)
        for j, i in enumerate(queryIndices):
            # If the replaced character is the same as the current, nothing changes
            if characters[i] == queryCharacters[j]:
                answers.append(lengths[-1])
                continue
            
            # Otherwise, find the replaced substring
            index = substrings.bisect_right((i, n)) - 1
            replaced = substrings.pop(index)
            lengths.remove(replaced[1] - replaced[0] + 1)
            
            # Split it if applicable
            if replaced[0] != i:
                substrings.add((replaced[0], i - 1))
                lengths.add(i - replaced[0])
            if replaced[1] != i:
                substrings.add((i + 1, replaced[1]))
                lengths.add(replaced[1] - i)

            # Replace the current character
            characters[i] = queryCharacters[j]

            # And replace it with the new substring, merging others if applicable
            replacement = (i, i)
            if i < n - 1 and characters[i] == characters[i + 1]:
                index = substrings.bisect_left((i, i))
                other = substrings.pop(index)
                lengths.remove(other[1] - other[0] + 1)
                replacement = (replacement[0], other[1])
            if i > 0 and characters[i] == characters[i - 1]:
                index = substrings.bisect_left((i, i))
                other = substrings.pop(index - 1)
                lengths.remove(other[1] - other[0] + 1)
                replacement = (other[0], replacement[1])

            # Adding it back into the lists
            substrings.add(replacement)
            lengths.add(replacement[1] - replacement[0] + 1)

            # Storing the current longest as the answer
            answers.append(lengths[-1])
        
        # Finally, return the answers after each of the queries
        return answers
