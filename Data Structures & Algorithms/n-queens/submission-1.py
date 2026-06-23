class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        
        def is_safe(row, col):
            r, c = row - 1, col - 1
            
            # left top diag
            while r >=0 and c >= 0:
                if board[r][c] == 'Q': return False
                r -= 1
                c -= 1
            
            r, c = row + 1, col - 1
            # left bottom diag
            while r < n and c >= 0:
                if board[r][c] == 'Q': return False
                r += 1
                c -= 1

            r, c = row, col - 1
            # left
            while c >= 0:
                if board[r][c] == 'Q': return False
                c -= 1

            return True
        
        def solve(col):
            nonlocal board
            if col == n:
                res.append([''.join(row) for row in board])
                return
            
            for row in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    solve(col + 1)
                    board[row][col] = '.'

        solve(0)
        return res