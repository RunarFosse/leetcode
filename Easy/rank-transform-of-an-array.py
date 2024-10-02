# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)

        # Sort the indices based on the original array in ascending order
        indices = sorted(range(n), key=lambda i: arr[i])
        
        # Iterate over every index in the sorted array
        ranks, rank = [0] * n, 1
        for i in range(n):
            # If the current element is larger than the last, increment rank
            if i and arr[indices[i]] > arr[indices[i-1]]:
                rank += 1
            
            ranks[indices[i]] = rank
        
        # Return array of ranks
        return ranks
        
