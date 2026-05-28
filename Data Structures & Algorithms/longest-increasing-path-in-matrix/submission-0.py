class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        
        def explore(r, c):
            if dp[r][c] != 0: return dp[r][c]

            max_path = 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    max_path = max(max_path, 1 + explore(nr, nc))

            dp[r][c] = max_path
            return dp[r][c]
        
        return max(explore(r, c) for r in range(ROWS) for c in range(COLS))
