# Author: Runar Fosse
# Time complexity: O(mnlog m)
# Space complexity: O(mn)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using lexicographical sorting
        anagrams = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(string)
        
        # Then output the list of lists
        return anagrams.values()
        
# We can iterate the list of strings, sorting each string in lexicographical
# order, and add the non-sorted list into a list in a hashmap, given by the
# key of the sorted string.

# This solution seems unoptimal, but is actually the best way to
# solve the given problem most efficiently.