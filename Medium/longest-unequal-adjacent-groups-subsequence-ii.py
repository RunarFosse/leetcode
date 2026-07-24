# Author: Runar Fosse
# Time complexity: O(mn^2)
# Space complexity: O(n)

# where m is the longest string in words

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # Using dynamic programming
        n = len(words)

        # Store optimal values, aswell as adjacent word in longest subsequence per i
        opt, adjacent = [1] * n, [-1] * n

        # Then, iterate every initial index
        best_index = n - 1
        for i in reversed(range(n - 1)):
            # Iterate every word after at index j
            for j in range(i + 1, n):
                # Ensure they have a differing group, and equal length
                if groups[i] == groups[j] or len(words[i]) != len(words[j]):
                    continue

                # If so, compute hamming distance, ensuring it is 1
                distance = self.hamming(words[i], words[j])
                if distance == 1 and opt[i] < 1 + opt[j]:
                    # If so, and it gives a maximum sequence, remember it
                    opt[i] = 1 + opt[j]
                    adjacent[i] = j
            
            # Also store the current index starting the longest valid subsequence
            if opt[i] > opt[best_index]:
                best_index = i
        
        # Finally, reconstruct the sequence of the best index
        sequence, index = [], best_index
        while index >= 0:
            sequence.append(words[index])
            index = adjacent[index]

        # And return it
        return sequence 
    
    def hamming(self, word1: str, word2: str) -> int:
        # Compute the hamming distance between two words of equal length
        distance = 0

        # By iterating their characters
        for c1, c2 in zip(word1, word2):
            # If characters are unequal, increment distance
            if c1 != c2:
                distance += 1

        return distance 


# opt(i) - The longest subsequence of words with index equal or higher than i,
#          where adjacent elements have unequal groups, are equal in length
#          and have a hamming distance of 1.

# Base case:
# opt(n) = 1

# Recurrency:
# opt(i) = max(1 + opt(j) for j in range(i + 1, n if valid))
#        where valid = group[i] != group[j] and len(word[i]) == len(word[j])
#                      and hamming(word[i], word[j]) == 1

# If using bottom-up dynamic programming we can also store the maximum j to each i,
# such that we can reconstruct the actual longest valid subsequence of words.

# No. states = n
# Time complexity per state -> O(n)
# Total time complexity => O(n^2)