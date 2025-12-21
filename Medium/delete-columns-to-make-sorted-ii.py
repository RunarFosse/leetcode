# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(m)

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Using greedy
        m, n = len(strs), len(strs[0])

        # Store an array denoting if two rows already are in lexicographical order
        correct = [False] * (m - 1)

        # Then, transpose the grid to get a list of columns
        transposed = zip(*strs)

        # Then iterate those columns
        deleted = 0
        for column in transposed:
            # If there is any pair that is not in relative lexicographical order
            if any(not correct[i] and column[i] > column[i+1] for i in range(m - 1)):
                # Then delete it
                deleted += 1
            else:
                # Otherwise, count rows which are strictly lexicographical ordered
                for i in range(m - 1):
                    if column[i] < column[i + 1]:
                        correct[i] = True
        
        # Finally, return the number of columns deleted
        return deleted
