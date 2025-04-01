# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Using dynamic programming
        self.n, self.questions = len(questions), questions
        return self.opt(0)

    @functools.cache
    def opt(self, i: int) -> int:
        if i >= self.n:
            return 0
        points, brainpower = self.questions[i]
        
        # Find the maximum between picking or skipping this question
        return max(points + self.opt(i + brainpower + 1), self.opt(i + 1))