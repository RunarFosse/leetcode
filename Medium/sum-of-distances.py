# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Using prefix sum
        n = len(nums)
        
        # Iterate the numbers
        indices = defaultdict(list)
        for i in range(n):
            # Storing indices of equal value
            indices[nums[i]].append(i)
        
        # Then, iterate every index group
        arr = [0] * n
        for group in indices.values():
            # Get the number of indices per this value
            occurences = len(group)

            # Keep a running prefix and suffix sum of indices
            prefix, suffix = 0, sum(group)

            # Then, iterate the indices
            for i in range(occurences):
                # Get the current index
                index = group[i]

                # Compute the value of arr[index] of the left and right
                left = i * index - prefix
                right = suffix - (occurences - i) * index
            
                # And set arr[index] equal to the sum
                arr[index] = left + right
                
                # And update the index prefix and suffix sum
                prefix += index
                suffix -= index

        # Finally, return the array arr
        return arr
