class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26

        for i in s:
            c1[ord(i) - ord('a')] += 1

        for i in t:
            c2[ord(i) - ord('a')] += 1

        return c1 == c2