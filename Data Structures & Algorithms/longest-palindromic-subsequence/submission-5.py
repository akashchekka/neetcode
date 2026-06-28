class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        for i1 in range(1, n+1):
            for i2 in range(1, n+1):
                if s[i1 - 1] == s[n - i2]:
                    curr[i2] = prev[i2 - 1] + 1
                else:
                    curr[i2] = max(prev[i2], curr[i2 - 1])
            prev, curr = curr, prev

        return prev[n]