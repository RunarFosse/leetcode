# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def clearStars(self, s: str) -> str:
        # Using greedy
        
        # Store character indices in an array of stacks
        indexOf = lambda c: ord(c) - ord("a")
        stacks = [[] for _ in range(26)]

        # Iterate the string
        removed = set()
        for i, c in enumerate(s):
            # If the character is a star
            if c == "*":
                # Remove it and the current smallest character to its left
                removed.add(i)
                for i in range(26):
                    if stacks[i]:
                        removed.add(stacks[i].pop())
                        break
                continue
            
            # Otherwise, add it to its stack
            stacks[indexOf(c)].append(i)
        
        # Finally, rebuild and return the string
        return "".join(c for i, c in enumerate(s) if i not in removed)