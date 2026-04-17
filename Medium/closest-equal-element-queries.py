# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(n)

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Using prefix sum
        n, m = len(nums), len(queries)

        # Iterate the array left-to-right, storing last seen index of elements
        left = [0] * n
        indices = {}
        for i in range(-n, n):
            # If we've passed the array once, start filling out last seen indices
            if i >= 0:
                left[i] = indices.get(nums[i], -n)
            
            # Store this index as the last seen for the current element
            indices[nums[i % n]] = i
        
        # Do the same again, just right-to-left
        right = [0] * n
        indices.clear()
        for i in reversed(range(2 * n)):
            if i < n:
                right[i] = indices.get(nums[i], -n)
            indices[nums[i % n]] = i
        
        # Then, iterate the queries
        for i in range(m):
            index = queries[i]
            # If a number's closest index is itself, we cannot answer the query
            if index - left[index] == n:
                queries[i] = -1
                continue
            
            # Otherwise, set the distance to the smallest
            queries[i] = min(index - left[index], right[index] - index)
        
        # Finally, return all the answered queries
        return queries
