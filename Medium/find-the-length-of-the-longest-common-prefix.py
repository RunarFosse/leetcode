# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m)

# As all numbers are less than 10^8, length of numbers are always less than 9.
# I.e. iterating the digits of a number can be done in constant time.

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Using tries
        class Node():
            def __init__(self):
                self.children = {}
                self.end = False

        # First generate a prefix trie out of the first array
        trie = Node()
        for number in arr1:
            current = trie
            for c in str(number):
                if c not in current.children:
                    current.children[c] = Node()
                current = current.children[c]
            current.end = True
        
        # Then iterate the second array, keeping track of longest 
        # common prefix between all numbers and the prefix trie
        longest = 0
        for number in arr2:
            current, node = 0, trie
            for c in str(number):
                if c not in node.children:
                    break
                node = node.children[c]
                current += 1
            longest = max(current, longest)
        
        # Return the longest common prefix
        return longest