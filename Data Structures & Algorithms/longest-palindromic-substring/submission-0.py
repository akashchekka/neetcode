class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxlen = 0

        def process(l, r):
            nonlocal res, maxlen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    res = s[l:r+1]
                    maxlen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i
            process(l, r)

            l, r = i, i + 1
            process(l, r)

        return res