# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justified = []

        i = 0
        row, rowLength = [], 0
        while i < len(words):
            word = words[i]
            wordLength = len(word)

            # If can add a word (and possibly space), do so
            if rowLength + wordLength <= maxWidth:
                row.append(word)
                rowLength += min(wordLength + 1, maxWidth)
                i += 1
            # If you can't add more, its time to concat row string
            else:
                rowString = ""
                wordsInRow = len(row)
                # If there is only one word, add this
                if wordsInRow == 1:
                    rowString = row[0]
                # If not, calculate how much space between each word, with remainder
                else:
                    spaces, spaceRem = divmod(maxWidth - rowLength + wordsInRow, wordsInRow - 1)
                    for word in row:
                        if rowString:
                            rowString += " " * spaces
                            # Remainder spaces are spread out evenly
                            if spaceRem:
                                rowString += " "
                                spaceRem -= 1 
                        rowString += word
                # Reset row and append string to justified (with remaining spaces)
                row = []
                rowLength = 0
                justified.append(rowString + " " * (maxWidth - len(rowString)))
        
        # Add last row with its rules
        if row:
            string = ""
            for word in row:
                if string:
                    string += " "
                string += word
            string += " " * (maxWidth - len(string))
            justified.append(string)

        return justified