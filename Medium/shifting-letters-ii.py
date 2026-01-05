# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Using prefix sum
        n = len(s)

        # Create an array holding shifts per character at start and end intervals
        prefixes = [0] * (n + 1)
        for start, end, direction in shifts:
            shift = 1 if direction else -1
            prefixes[start] += shift
            prefixes[end + 1] -= shift
        
        # And add subsequent shifts together making it a prefix array
        for i in range(n):
            prefixes[i + 1] += prefixes[i]

        # Finally, iterate the string
        string = [""] * n
        for i in range(n):
            # Get the number of shifts at this index
            shifts = prefixes[i]

            # Extract the current character, and shift it, and add it to the string
            shifted = ord(s[i]) - ord("a") + shifts
            character = chr(shifted % 26 + ord("a"))
            string[i] = character
        
        # Then, return the resulting string
        return "".join(string)
