# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # First count occurences
        occurences = defaultdict(int)
        for num in arr:
            occurences[num] += 1
        
        # Then ensure no two n.o. occurences are equal
        occured = set()
        for occurence in occurences.values():
            if occurence in occured:
                return False
            occured.add(occurence)
        
        return True