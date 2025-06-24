# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)

        # First, find the indices of each key in the array
        keys = deque([i for i in range(n) if nums[i] == key])
        print(keys)

        # Then, iterate the array again, over possible k-distant indices
        indices = []
        start, end = max(keys[0] - k, 0), min(keys[-1] + k + 1, n)
        for i in range(start, end):
            # Remove key if they are out of range
            while keys and keys[0] < i - k:
                keys.popleft()
            
            # If there are remaining keys, check and count as valid index
            if not keys:
                break
            elif abs(keys[0] - i) <= k:
                indices.append(i)
        
        # Finally, return the number of k-distant indices
        return indices