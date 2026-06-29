class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        nxt, nxtnxt = 1, 0
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                curr = nxt

                if i + 1 < n and int(s[i: i+2]) <= 26:
                    curr += nxtnxt

            nxtnxt = nxt
            nxt = curr    
        return curr