# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n^2)

class Solution:
    def maximumLength(self, s: str) -> int:
        # Using sliding window
        occurences = defaultdict(int)

        current = deque([])
        for c in s:
            # Find current special substring
            removals = 0
            while current and c != current[0]:
                # And count occurences when removing last
                occurences[(current[0], len(current))] += removals + 1
                current.popleft()
                removals += 1

            current.append(c)
        
        # After iterating, count the last remaining substrings
        removals = 0
        while current:
            # Count occurences when removing previous
            occurences[(current[0], len(current))] += removals + 1
            current.popleft()
            removals += 1
        
        # Finally, count and return longest substring occuring thrice
        lengths = [string[1] for string, n in occurences.items() if n >= 3]
        return max(lengths) if lengths else -1
