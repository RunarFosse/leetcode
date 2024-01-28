# Author: Runar Fosse
# Time complexity: O(m^2n)
# Space complexity: O(m)

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # Using prefix sum
        m, n = len(matrix), len(matrix[0])

        # For each possible submatrix height,
        # count no_submatrices which sum to target
        result = 0
        for height in range(m):
            prefix_rows = [0] * n
            for i, row in enumerate(matrix):
                # Calculate prefix_sum over all rows in current submatrix
                prefix_sum, subtrahend = 0, 0
                for j, num in enumerate(row):
                    if i > height:
                        subtrahend += matrix[i-height-1][j]
                    prefix_sum += num
                    prefix_rows[j] += prefix_sum - subtrahend
                
                # Count number of subarrays which sum to target,
                # if submatrix height has been reached
                if i < height:
                    continue

                sums = defaultdict(int)
                for prefix_sum in prefix_rows:
                    if prefix_sum == target:
                        result += 1
                    
                    if prefix_sum - target in sums:
                        result += sums[prefix_sum - target]

                    sums[prefix_sum] += 1
        
        return result
                        

# Prefix sum over each row in the array, then we can iterate for every submatrix
# height, iterating the sum of rows (acting as if it was a 1d array) and counting
# the number of subarrays which sum to target.