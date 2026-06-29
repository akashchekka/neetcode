class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}
        memo[n] = 1

        def dp(i):
            if i in memo: return memo[i]
            if s[i] == '0': return 0

            res = dp(i + 1)
            if i + 1 < n and int(s[i: i+2]) <= 26:
                res += dp(i + 2)

            memo[i] = res
            return res
        
        return dp(0)