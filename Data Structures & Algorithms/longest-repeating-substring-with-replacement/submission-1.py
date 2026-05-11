class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxLen = maxF = 0
        c = defaultdict(int)

        for r in range(len(s)):
            c[s[r]] += 1
            maxF = max(maxF, c[s[r]])

            if (r - l + 1) - maxF > k:
                c[s[l]] -= 1
                l += 1
            else:
            # if (r - l + 1) - maxF <= k:
                maxLen = max(maxLen, r - l + 1)
        
        return maxLen
