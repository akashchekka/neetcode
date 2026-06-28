class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[''] * (n + 1) for _ in range(n + 1)]
        for i1 in range(1, n+1):
            for i2 in range(1, n+1):
                if s[i1 - 1] == s[n - i2]:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1] + s[i1 - 1]
                else:
                    dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1], key=len)

        return len(dp[n][n])