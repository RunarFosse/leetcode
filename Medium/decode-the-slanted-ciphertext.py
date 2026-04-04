# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # First, compute the number of columns in the matrix
        columns = len(encodedText) // rows

        # Then, iterate the matrix and decode the cipher text
        string = []
        for j in range(columns):
            for i in range(min(rows, columns - j)):
                string.append(encodedText[j + i * (columns + 1)])
        
        # Remove any trailing spaces
        while string and string[-1] == " ":
            string.pop()
        
        # And finally, return the original text
        return "".join(string)
