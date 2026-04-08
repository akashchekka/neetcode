class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        rows, cols = len(grid), len(grid[0])

        def explore(r, c):
            # Check r and c boundaries
            rowInbounds = 0 <= r < rows
            colInbounds = 0 <= c < cols
            if not rowInbounds or not colInbounds: return False
            
            # Check if its water
            if grid[r][c] == '0': return False

            pos = (r, c)
            if pos in visited: return False

            visited.add(pos)

            explore(r - 1, c)
            explore(r + 1, c)
            explore(r, c - 1)
            explore(r, c + 1)

            return True

        for i in range(rows):
            for j in range(cols):
                if explore(i, j):
                    count += 1

        return count