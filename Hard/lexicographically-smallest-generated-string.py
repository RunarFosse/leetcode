# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(m + n)

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        # Using greedy
        n, m = len(str1), len(str2)

        # First, initialize the word with 0 characters set
        word = [None] * (n + m - 1)

        # Also, store characters which are forced to take on their value
        forced = [False] * (n + m - 1)

        # Then, iterate the first string
        for i in range(n):
            if str1[i] == "F":
                continue
            
            # And set the character's we can guarantee are correct
            for j in range(m):
                # Ensuring, that we find no mismatch
                if word[i + j] is not None and word[i + j] != str2[j]:
                    # If so, the word is invalid
                    return ""
                word[i + j] = str2[j]
                forced[i + j] = True
        
        # Then, set every unset character to the smallest character 'a'
        for i in range(n + m - 1):
            if word[i] is None:
                word[i] = "a"
        
        # Then iterate the first string again
        for i in range(n):
            if str1[i] == "T":
                continue
            
            # Ensuring that no substring spells out str2
            if not "".join(word[i:i+m]) == str2:
                continue
            
            # But if it does, greedily set the rightmost non-forced position to 'b'
            valid = False
            for j in reversed(range(m)):
                if forced[i + j]:
                    continue
                
                word[i + j] = "b" if str2[j] == "a" else "a"
                valid = True
                break
            
            # If no character could be changed, the word remains invalid
            if not valid:
                return ""

        # Finally, return the valid lexicographically smallest word
        return "".join(word)
