class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        self.x = False
        m, n = len(board), len(board[0])

        def dfs(b, i, j, k, s):
            if k == len(s):
                self.x = True
                return

            if i < 0 or j < 0 or i >= len(b) or j >= len(b[0]) or b[i][j] != s[k]:
                return 

            temp = b[i][j]
            b[i][j] = '#' 
            
            dfs(b, i - 1, j, k + 1, s)
            dfs(b, i, j - 1, k + 1, s)
            dfs(b, i + 1, j, k + 1, s)
            dfs(b, i, j + 1, k + 1, s)

            b[i][j] = temp

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    dfs(board, i, j, 0, word)
                    if self.x:
                        return True
        return False