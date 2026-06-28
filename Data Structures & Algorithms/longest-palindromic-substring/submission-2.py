class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        res = ""

        def process(l, r):
            nonlocal res, maxlen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    maxlen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1

        for i in range(len(s)):
            process(i, i)
            process(i, i+1)

        return res