# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # Iterate the elements
        seen, minimum, maximum = set(), inf, -inf
        for num in nums:
            # Mark all elements that are present in the array
            seen.add(num)

            # And store maximum and minimum entries
            maximum = max(num, maximum)
            minimum = min(num, minimum)
        
        # Then, iterate the original range
        missing = []
        for num in range(minimum, maximum):
            # If they are not a part of the current array
            if num not in seen:
                # Add them as missing
                missing.append(num)
        
        # And return every missing element
        return missing
