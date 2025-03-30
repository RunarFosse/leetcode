# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)

        # First compute the last occurence of each character
        indexOf = lambda c: ord(c) - ord("a")
        occurences = [0] * 26
        for i in range(n):
            occurences[indexOf(s[i])] = i
        
        # Reiterate the string, computing split index of each partition
        partitions = []
        end, size = 0, 0
        for i in range(n):
            # First, extend current end of partition
            end = max(occurences[indexOf(s[i])], end)
            size += 1

            # Then, check if we can validly split here
            if i == end:
                partitions.append(size)
                size = 0
        
        # Finally, return size of each partition
        return partitions
