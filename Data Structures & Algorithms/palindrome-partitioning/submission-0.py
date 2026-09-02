class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(i, j):
            return s[i:j+1] == s[i:j+1][::-1]

        current = []
        def backtrack(i):
            if i == len(s):
                res.append(current[:])
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    current.append(s[i:j+1])
                    backtrack(j+1)
                    current.pop()

        backtrack(0)
        return res