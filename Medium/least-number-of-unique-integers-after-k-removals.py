# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Using counting sort
        n = len(arr)

        # Count occurence of each number, in sorted order
        occurences = defaultdict(int)
        for num in arr:
            occurences[num] += 1
        
        # Sort the values in ascending order (using counting sort)
        numbers_occured = [0] * (n+1)
        unique_occurences = 0
        for occurence in occurences.values():
            unique_occurences += 1
            numbers_occured[occurence] += 1

        # Remove maximum number of unique integers
        for occurences in range(1, n+1):
            if k < occurences:
                break
            
            unique_occurences -= min(k // occurences, numbers_occured[occurences])
            k -= numbers_occured[occurences] * occurences
        
        # Return the number of integers which remain
        return unique_occurences