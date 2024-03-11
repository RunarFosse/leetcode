# Author: Runar Fosse
# Time complexity: O(m+n)
# Space complexity: O(n)

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Using counting sort
        frequencies = defaultdict(int)
        for c in s:
            frequencies[c] += 1
        
        # Iterate "order", creating sorted string from frequency array
        characters = []
        for c in order:
            characters.append(c * frequencies[c])
            frequencies[c] = 0
        
        # Then add all characters omitted in "order"
        characters += [c * freq for c, freq in frequencies.items() if freq]
        
        # Return the resulting string
        return "".join(characters)