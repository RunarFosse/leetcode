# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # Using two pointer
        n = len(word)

        # If we only have 1 friend, they get the whole word
        if numFriends == 1:
            return word

        # If we give all but 1 friend a word of size 1,
        # the last friend will get a word of length
        length = n - numFriends + 1

        # Iterate the word
        substring = ""
        for i in range(n):
            # Storing the largest lexicographic substring
            substring = max(word[i:i + length], substring)
        
        # Finally, return it
        return substring