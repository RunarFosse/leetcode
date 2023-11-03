# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        num, i = 1, 0
        while i < len(target):
            stack.append("Push")
            if target[i] == num:
                i += 1
            else:
                stack.append("Pop")
            num += 1
        return stack