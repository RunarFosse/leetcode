# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        n = len(sentence)

        # First verify that the first and last letter are equal
        if sentence[0] != sentence[-1]:
            return False
        
        # Then verify that every word does the same
        pointer = 0
        while pointer < n:
            splitsWord = sentence[pointer] == " "
            if splitsWord and sentence[pointer-1] != sentence[pointer+1]:
                return False
            pointer += 1
            
        return True
