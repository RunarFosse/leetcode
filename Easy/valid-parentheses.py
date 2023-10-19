# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for i in range(n := len(s)):
            if c2 := {"(": ")", "[": "]", "{": "}"}.get(s[i]):
                queue.append(c2)
                continue

            if len(queue) > n - i or not queue or s[i] != queue.pop():
                return False
        
        return len(queue) == 0

