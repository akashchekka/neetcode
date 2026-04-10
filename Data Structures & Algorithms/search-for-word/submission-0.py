class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, index):
            if index == len(word): return True

            if (not (0 <= r < rows) or 
                not (0 <= c < cols) or 
                board[r][c] != word[index] or
                (r, c) in visited) : return False

            visited.add((r, c))
            isValid = False

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                isValid = isValid or dfs(nr, nc, index + 1)

            visited.remove((r, c))
            return isValid

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False