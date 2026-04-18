class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        capture = []

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    capture.append((r, c))

        def convert(r, c):
            nonlocal capture
            for i in range(cols):
                matrix[r][i] = 0
                if (r, i) not in capture:
                    visited.add((r, i))

            for j in range(rows):
                matrix[j][c] = 0
                if (j, c) not in capture:
                    visited.add((j, c))

        for r, c in capture:
            if (r, c) not in visited:
                convert(r, c)
        