# Author: Runar Fosse
# Time complexity: O(n + (m + k)log k)
# Space complexity: O(m + k)

# where k is the maximum element in the array

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # Using counting sort

        # Find the maximum value in the array
        maximum = max(nums)

        # Then, compute the GCD between any pair of numbers by first counting frequencies
        gcds = [0] * (maximum + 1)
        for num in nums:
            gcds[num] += 1
        
        # Then, add together all counts divisible by a lower number
        for i in range(1, maximum + 1):
            # By summing count multiples of i
            for j in range(i * 2, maximum + 1, i):
                gcds[i] += gcds[j]
        
        # Replace count of elements divisible to count of pairs of 2 where one divides
        for i in range(maximum + 1):
            gcds[i] = gcds[i] * (gcds[i] - 1) // 2
        
        # Finally, remove all counts of pairs with a higher actual GCD
        # (original pairs where the first element strictly divides the second)
        for i in reversed(range(1, maximum + 1)):
            for j in range(i * 2, maximum + 1, i):
                gcds[i] -= gcds[j]
        
        # Then, compute the prefix sum of GCDs
        prefixes = list(accumulate(gcds))
        
        # Finally, iterate the queries
        answers = []
        for index in queries:
            # Binary search the GCD of the queried index
            answer = bisect_right(prefixes, index)
            answers.append(answer)
        
        # And return the resulting query answers
        return answers
