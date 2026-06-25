# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Using prefix sum
        n = len(nums)

        # Store the frequency of different prefix sums (with prefix shifted by n)
        frequencies = [0] * n + [1] + [0] * n

        # Also store the number of valid majority subarrays ending at each index
        valids = 0

        # Iterate the array
        subarrays, prefix = 0, n
        for num in nums:
            # If the current number is equal to the target
            if num == target:
                # First, increment the prefix sum, and frequency count
                prefix += 1
                frequencies[prefix] += 1

                # Then, add the number of smaller prefixes to the valids
                valids += frequencies[prefix - 1]
            else:
                # Otherwise, decrement the prefix sum
                prefix -= 1

                # Remove all occurences of subarrays which are now not majority anymore
                valids -= frequencies[prefix]

                # Increment the frequenciy of the prefix
                frequencies[prefix] += 1

            # Finally, add all currently valid subarrays to the count
            subarrays += valids
        
        # And return them
        return subarrays
