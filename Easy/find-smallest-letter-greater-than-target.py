# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Using binary search
        n = len(letters)

        # Find the first character greater than target
        index = bisect_right(letters, target)

        # Return said character, if it exists, if not, return the first character
        return letters[index] if index < n else letters[0]
