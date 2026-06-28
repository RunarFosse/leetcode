# Author: Runar Fosse
# Time complexity: O(nlog(log(m)))
# Space complexity: O(n)

# with m being the largest element in the array

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # First, count the frequencies of the numbers in the array
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        
        # Initialize the largest subset as largest odd number of all 1s
        maximum = frequencies.pop(1, 0)
        if maximum and not maximum % 2:
            maximum -= 1

        # Finally, iterate all other numbers' frequencies
        for num in frequencies.keys():
            # And compute the size of the subset starting at this element
            current, subset = num, 0
            while current in frequencies and frequencies[current] >= 2:
                subset += 2
                current = pow(current, 2)
            
            # Compute the if the middle element is the current or previous number
            subset += 1 if current in frequencies else -1

            # And store the largest subset size
            maximum = max(subset, maximum)
        
        # Finally, return this maximum subset size
        return maximum
