class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        n = len(wordDict)

        def dp(target):
            if target in memo: return memo[target]
            if target == '': return True
            
            for word in wordDict:
                if target.startswith(word):
                    suffix = target.removeprefix(word)
                    if dp(suffix):
                        memo[target] = True
                        return True
            
            memo[target] = False
            return False

        return dp(s)