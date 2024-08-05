# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Store occurences of strings in the array
        occurences = defaultdict(int)

        # First iterate the array, removing non-distinct strings
        for string in arr:
            occurences[string] += 1
        
        # Then return the k'th distinct string
        for string in arr:
            if occurences[string] == 1:
                k -= 1
            
            if not k:
                return string
    
        # If there is no such k'th distinct string, return the empty string
        return ""
        