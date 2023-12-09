# Author: Runar Fosse
# Time complexity: O(mn2^k)
# Space complexity: O(k)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Using DFS
        self.m, self.n = len(board), len(board[0])
        self.k = len(word)
        self.word = word

        # Iterate every character, searching for the first letter in word
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                # If we've found it, start DFS
                if char == word[0] and self.dfs((i,j), 0, board):
                    return True
                    
        return False
    
    def dfs(self, pos: (int, int), index: int, board: List[List[str]]) -> bool:
        # DFS from position
        i, j = pos
                        
        # If index is equal to length of word, we have found our word
        if index == self.k-1:
            return True

        # Temporarily modify board before continuing DFS
        board[i][j] = ""
                        
        # DFS all surrounding chars which match word[index+1]
        found = False
        for y, x in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            if y < 0 or y >= self.m or x < 0 or x >= self.n:
                continue
            if board[y][x] == self.word[index+1] and self.dfs((y,x), index+1, board):
                found = True
                break
        
        # After DFS, restore original board
        board[i][j] = self.word[index]

        return found