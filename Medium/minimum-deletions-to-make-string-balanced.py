# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0

        # Iterate every character
        total_b = 0
        for c in s:
            # If we see an a
            if c == "a":
                # We can choose to either delete it, or delete
                # every b before it to make string balanced
                deletions = min(total_b, deletions + 1)
            else:
                total_b += 1
        
        return deletions
        