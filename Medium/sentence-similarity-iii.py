# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # First split each sentence into words
        sentence1, sentence2 = sentence1.split(" "), sentence2.split(" ")

        # Force the first sentence to be the longest
        if len(sentence1) < len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        
        # And turn the second sentence into a double ended queue
        sentence2 = deque(sentence2)
        
        # Iterate sentence1 from front-to-back and back-to-front,
        # verifying that it is a superset of sentence2,
        # strictly separated by a contiguous sequence of words
        for word in sentence1:
            if not sentence2 or word != sentence2[0]:
                break
            sentence2.popleft()
        for word in reversed(sentence1):
            if not sentence2 or word != sentence2[-1]:
                break
            sentence2.pop()
        
        # Now, the two sentences are similar if sentence2 is empty
        return not len(sentence2)
        