# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Using greedy

        # First, count the frequency of each character in the string
        indexOf = lambda c: ord(c) - ord("a")
        frequencies = [0] * 26
        for c in s:
            frequencies[indexOf(c)] += 1
        
        # Then, iterate the string again
        stack, visited = [], [False] * 26
        for c in s:
            # If the current character is not already in the subsequence
            if not visited[indexOf(c)]:
                # Remove all the larger characters
                while stack and stack[-1] > c:
                    # However do not pop off any characters no longer in s
                    if frequencies[indexOf(stack[-1])] == 0:
                        break
                    
                    visited[indexOf(stack.pop())] = False
            
                # Then, add it to its earliest possible position
                visited[indexOf(c)] = True
                stack.append(c)
            
            # And remove one of this character from s
            frequencies[indexOf(c)] -= 1
        
        # Finally, return the smallest subsequence which is in our stack
        return "".join(stack)
