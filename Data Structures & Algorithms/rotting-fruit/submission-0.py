class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        minutes = 0
        while q and fresh:
            minutes += 1

            for _ in range(len(q)):
                iters = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                r, c = q.popleft()
                for dr, dc in iters:
                    if ((0 <= r + dr < rows) and (0 <= c + dc < cols) and grid[r + dr][c + dc] == 1):
                        grid[r + dr][c + dc] = 2
                        q.append((r + dr, c + dc))
                        fresh -= 1

        return minutes if fresh == 0 else -1