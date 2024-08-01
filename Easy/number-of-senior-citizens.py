# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # Count passengers who are older than 60
        seniors = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                seniors += 1

        return seniors