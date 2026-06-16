# Author: Runar Fosse
# Time complexity: O(2^n)
# Space complexity: O(2^n)

class Solution:
    def processStr(self, s: str) -> str:
        # Store the resulting string in a deque
        result = deque([])

        # Iterate the string
        reverse = False
        for c in s:
            # Given the current character, apply its respective operation
            match c:
                # Either remove the last character from result
                case '*':
                    if result:
                        if reverse:
                            result.popleft()
                        else:
                            result.pop()
                # Duplicate and append the current result
                case '#':
                    result += result
                # Reverse the current result
                case '%':
                    reverse = not reverse
                # Or append the current character
                case _:
                    if reverse:
                        result.appendleft(c)
                    else:
                        result.append(c)
        
        # If the result should be reversed, do so
        if reverse:
            result.reverse()
        
        # Finally, return the resulting string
        return "".join(result)
