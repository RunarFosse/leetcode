# Author: Runar Fosse
# Time complexity: O(m2^n)
# Space complexity: O(n)

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Using DFS
        self.n = len(words)
        self.words, self.score = words, score

        # First compute a frequency list of our letters array
        self.indexOf = lambda c : ord(c) - ord("a")
        self.frequencies = [0] * 26
        for c in letters:
            self.frequencies[self.indexOf(c)] += 1
        
        # Return the maximum possible score for a valid subset
        return self.dfs(0)

    def dfs(self, i: int) -> int:
        # If we've reached the end, return base score
        if i == self.n:
            return 0
        
        # Check score skipping current word
        max_score = self.dfs(i+1)

        # Before checking score picking this word we decrement frequencies
        valid = True
        current_score = 0
        for j in range(len(self.words[i])):
            c = self.words[i][j]
            self.frequencies[self.indexOf(c)] -= 1
            current_score += self.score[self.indexOf(c)]
            if self.frequencies[self.indexOf(c)] < 0:
                valid = False
                break
        
        # If picking this word makes subset stay valid, recurse and compare
        if valid:
            max_score = max(current_score + self.dfs(i+1), max_score)

        # Then backtrack by adding current word frequencies back
        for k in range(j+1):
            c = self.words[i][k]
            self.frequencies[self.indexOf(c)] += 1
        
        # And return current max score
        return max_score
