# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Using bitmasks
        n = len(word)
        occurences = [0] * (1 << 10)
        occurences[0] = 1

        substrings, prefix = 0, 0
        for c in word:
            # Compute current prefix bitmask
            bit = ord(c) - ord("a")
            prefix ^= (1 << bit)
            
            # Add all previous occurences with a bitmask difference <= 1
            substrings += occurences[prefix]
            for i in range(10):
                substrings += occurences[prefix ^ (1 << i)]

            # And increment current prefix's occurence
            occurences[prefix] += 1

        # Return all wonderful substrings
        return substrings

# Store prefix bitmasks where each bit represents a letter. A bit is set if 
# a letter has appeared an odd amount of times previously. For each bitmask
# we need to check if if any other bitmask with a difference <= 1 has occured
# previously. If so, they together make a wonderful substring!