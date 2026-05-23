class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        arr = [False] * (n + 1)
        arr[0] = True

        for i in range(n + 1):
            for j in wordDict:
                if arr[i] and i + len(j) <= n and s.startswith(j, i):
                    arr[i + len(j)] = True
        
        return arr[n]