class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        count = 0
        rows, cols = len(grid), len(grid[0])

        def explore(r, c):
            if ((not (0 <= r < rows) or not (0 <= c < cols)) or
                grid[r][c] == 0 or
                (r, c) in visited): return 0

            visited.add((r, c))

            size = 1 + explore(r - 1, c) + explore(r + 1, c) + explore(r, c - 1) + explore(r, c + 1)

            return size

        for i in range(rows):
            for j in range(cols):
                count = max(count, explore(i, j))

        return count