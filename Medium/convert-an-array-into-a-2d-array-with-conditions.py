# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Count frequency and conditioned 2D array
        array = []
        frequencies = [0 for _ in range(200)]
        for num in nums:
            # Retrieve and update frequency
            frequency = frequencies[num-1]
            frequencies[num-1] = frequency+1

            # Add into 2D array placed respectively to its previous frequency
            if len(array) <= frequency:
                array.append([num])
            else:
                array[frequency].append(num)

        
        return array


# Store each numbers frequency in an array.
# For each row in the 2D output array, iterate this frequency array.
# For each number with a current frequency > 0, add said number to the current
# row in the output array and decrement its frequency value.

# Note, instead of iterating the frequency array after, we can keep the frequency
# of a current number as the "row index in which to insert num".
# In this way, we can create the 2D output array simultaneously!

# Space complexity is O(n) as all elements in the 2D output array
# are contained in the nums input array.