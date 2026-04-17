# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # Using two pointer approach
        n = len(words)

        # Iterate all distances from the start
        for distance in range(n // 2 + 1):
            # Check walking left or right
            left = (startIndex - distance) % n
            right = (startIndex + distance) % n

            # If either element is equal to target, return the distance
            if words[left] == target or words[right] == target:
                return distance
        
        # If loop terminates, then target does not exist in words
        return -1
