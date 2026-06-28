class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def recurse(i1, i2):
            if i1 < 0 or i2 < 0:
                return 0
            if (i1, i2) in memo: return memo[(i1, i2)]
            
            res = 0
            if text1[i1] == text2[i2]:
                res = 1 + recurse(i1 - 1, i2 - 1)
            else:
                res = max(recurse(i1 - 1, i2), recurse(i1, i2 - 1))
            
            memo[(i1, i2)] = res
            return memo[(i1, i2)]
        
        return recurse(len(text1) - 1, len(text2) - 1)